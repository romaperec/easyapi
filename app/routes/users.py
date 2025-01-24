from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from schemas.schemas import UserAddSchema
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

@user_router.post("/create_user")
async def create_user(user: UserAddSchema, db: AsyncSession = Depends(get_db)):
    new_user = UsersModel(name=user.name, description=user.description)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {"message": "success"}