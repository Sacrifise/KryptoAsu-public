from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from routers import post_router as p_rout
from routers import get_rout as g_rout
from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Очищена")
    await create_tables()
    print("Готова к работе")
    yield
    print("Выключение")
    
results: List[dict] = []
async def get_results() -> List[dict]:
    return results

app = FastAPI(lifespan=lifespan)
app.include_router(p_rout)
app.include_router(g_rout)