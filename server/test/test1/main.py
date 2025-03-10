from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from routers import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Очищена")
    await create_tables()
    print("Готова к работе")
    yield
    print("Выключение")
    
    
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
