from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, drop_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print('Base dropped')
    await create_tables()
    print('Base created')
    yield
    print('Turning off')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
