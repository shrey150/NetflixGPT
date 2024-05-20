from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from config import settings

DB_DRIVER_URI = str(settings.DB_CONNECTION_URI).replace(
    "postgresql", "postgresql+psycopg"
)

engine = create_async_engine(
    DB_DRIVER_URI, connect_args={"sslmode": "require"}, pool_recycle=300
)

async_session = sessionmaker(
  engine,
  class_= AsyncSession,
  expire_on_commit=False,
)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def async_get_db() -> AsyncSession:
    local_session = async_session

    async with local_session() as db:
        yield db
        await db.commit()
