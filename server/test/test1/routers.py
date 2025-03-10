from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import GCD_LCM
from repository import TaskRepository
from functools import reduce
from math import gcd, lcm

router = APIRouter(
    prefix="/Operations",
    tags=["Operations"]
)

@router.post(
    "/GCD",
    summary="НОД"
)
async def GCD(
    response: Annotated[GCD_LCM, Depends()],
):
    results.append(reduce(gcd, response.value)

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {"data": tasks}