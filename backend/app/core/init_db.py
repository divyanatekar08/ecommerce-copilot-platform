import asyncio
from app.core.database import engine
from app.models.ecommerce import Base

async def init_tables():
    async with engine.begin() as conn:
        print("Creating PostgreSQL tables...")
        await conn.run_sync(Base.metadata.create_all)
        print("Database tables created successfully!")

if __name__ == "__main__":
    asyncio.run(init_tables())