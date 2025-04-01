from fastapi import APIRouter, Depends
from schemas import GreaterCommonDivisor, LeastCommonMultiple, ModuleСomparison
from functools import reduce
from math import gcd, lcm
from functions import solve_congruence

router = APIRouter(
    prefix='/operations',
    tags=["operations"]
)

@router.post(
    "/gcd",
    summary="нод"
)
async def greater_common_divisor(
    response: GreaterCommonDivisor
):
    result = reduce(gcd, response.elements)
    return {
        "success": True,
        "value": response.elements,
        "result": result
    }
  
@router.post(
    "/lcm",
    summary="нок"
)
async def least_common_multiple(
    response: LeastCommonMultiple
):
    result = reduce(lcm, response.elements)
    return {
        "success": True,
        "value": response.elements,
        "result": result
    }
    
@router.post(
    "/module",
    summary="модуль"
)
async def module_comprasion(
    response: ModuleСomparison
):
    result = solve_congruence(response.elements)
    if result is None:
        return {
            "success": True,
            "value": response.elements,
            "result": "Решений нет"
        }
    else:
        return {
            "success": True,
            "value": response.elements,
            "result": result
        }