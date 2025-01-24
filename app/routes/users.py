from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from models.models import UsersModel
from database import AsyncSession, async_session

user_router = APIRouter(prefix="/users", tags=["Users 🚀"])


async def get_db():
    async with async_session() as session:
        yield session


@user_router.get("/")
async def get_all_users(db: AsyncSession = Depends(get_db)):
    response = await db.execute(select(UsersModel))
    users = response.scalars().all()
    
    if not users:
        return HTTPException(status_code=204, detail="DataBase is empty")
    return users