from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, EmailStr, Field

# User Schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: Optional[str] = "customer"

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

# Product & Variant Schemas
class ProductVariantCreate(BaseModel):
    sku: str
    size: Optional[str] = None
    color: Optional[str] = None
    stock_quantity: int = 0
    price_override: Optional[float] = None

class ProductVariantResponse(ProductVariantCreate):
    id: int
    product_id: int

    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
    category: str
    base_price: float
    variants: List[ProductVariantCreate] = []

class ProductResponse(BaseModel):
    id: int
    name: str
    slug: str
    description: Optional[str]
    category: str
    base_price: float
    is_active: bool
    variants: List[ProductVariantResponse] = []

    class Config:
        from_attributes = True

# Order & Checkout Schemas
class OrderItemCreate(BaseModel):
    variant_id: int
    quantity: int
    unit_price: float

class CreateCheckoutSession(BaseModel):
    items: List[OrderItemCreate]
    shipping_address: Dict[str, Any]

class PaymentIntentResponse(BaseModel):
    client_secret: str
    payment_intent_id: str
    order_id: int
    total_amount: float