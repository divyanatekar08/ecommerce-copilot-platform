import stripe
from fastapi import APIRouter, Depends, HTTPException, Request, Header, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import settings
from app.core.database import get_db
from app.models.ecommerce import Order, OrderItem, ProductVariant
from app.schemas.ecommerce import CreateCheckoutSession, PaymentIntentResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/create-payment-intent", response_model=PaymentIntentResponse)
async def create_payment_intent(
    payload: CreateCheckoutSession,
    db: AsyncSession = Depends(get_db)
):
    """
    1. Calculates total amount from payload.
    2. Inserts an order in 'pending' status in PostgreSQL.
    3. Creates a Stripe PaymentIntent and links it to the order.
    """
    total_amount = sum(item.quantity * item.unit_price for item in payload.items)
    
    # 1. Create Pending Order record in DB
    new_order = Order(
        total_amount=total_amount,
        shipping_address=payload.shipping_address,
        status="pending"
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    # 2. Add Order Items
    for item in payload.items:
        order_item = OrderItem(
            order_id=new_order.id,
            variant_id=item.variant_id,
            quantity=item.quantity,
            unit_price=item.unit_price
        )
        db.add(order_item)
    
    await db.commit()

    # 3. Create Stripe PaymentIntent (Amount in cents)
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),
            currency="usd",
            metadata={"order_id": new_order.id}
        )

        # Update order with Stripe PaymentIntent ID
        new_order.stripe_payment_intent_id = intent.id
        await db.commit()

        return PaymentIntentResponse(
            client_secret=intent.client_secret,
            payment_intent_id=intent.id,
            order_id=new_order.id,
            total_amount=total_amount
        )
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Stripe PaymentIntent creation failed: {str(e)}"
        )

@router.post("/webhook")
async def stripe_webhook(
    request: Request,
    stripe_signature: str = Header(None),
    db: AsyncSession = Depends(get_db)
):
    """
    Listens for asynchronous Stripe webhooks to verify payment completion and update order status.
    """
    payload = await request.body()

    try:
        event = stripe.Webhook.construct_event(
            payload, stripe_signature, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Handle PaymentIntent Success
    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        order_id = payment_intent["metadata"].get("order_id")

        if order_id:
            result = await db.execute(select(Order).where(Order.id == int(order_id)))
            order = result.scalars().first()
            if order:
                order.status = "paid"
                await db.commit()

    return {"status": "success"}