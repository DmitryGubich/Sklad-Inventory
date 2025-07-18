from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import init_db, get_session
from app.models import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/users/")
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User))
    return result.all()
