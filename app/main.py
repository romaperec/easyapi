from fastapi import FastAPI

from database import engine
from routes.users import user_router
from models.models import Base

app = FastAPI(title="EasyAPI", version="0.1.2")
app.include_router(user_router)


@app.post("/setup_database", tags=["Danger zone 🩸"])
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        return {"message": "success"}
    