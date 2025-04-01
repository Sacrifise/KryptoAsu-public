from fastapi import APIRouter, Depends
from typing import Annotated, List
from schemas import GCD_LCM_ABS
from repository import Request_Repository
from functools import reduce
from math import gcd, lcm
from functions import solve_congruence
from sqlalchemy.exc import NoResultFound

# results: List[dict] = []
# async def get_results() -> List[dict]:
#     return results

post_router = APIRouter(
    prefix="/operations",
    tags=["operations"]
)

get_rout = APIRouter(
    prefix="/get",
    tags=["get"]
)


@post_router.post(
    "/gcd",
    summary="НОД"
)
async def GCD(
    response: Annotated[GCD_LCM_ABS, Depends()],
    #results: List[dict] = Depends(get_results)
):
    result = reduce(gcd, response.value)
    # results.append(
    #     {
    #         "value": response.value,
    #         "results": result
    #     }
    #)   
    new_operation_id = await Request_Repository.add_one_GCD_LCM_ABS(result)
    return {
        "success": True,
        "id": new_operation_id
        }
    
    
@post_router.post(
    "/lcm",
    summary="НОК")
async def LCM(
    response: GCD_LCM_ABS,
    #results: List[dict] = Depends(get_results)
    ):
    result = reduce(lcm, response.value)
    # results.append(
    #     {
    #         "value": response.value,
    #         "results": result
    #     }
    # )
    new_operation_id = await Request_Repository.add_one_GCD_LCM_ABS(result)
    return {
        "success": True,
        "id": new_operation_id
        }

# @post_router.post(
#     "/abs",
#     summary="Сравнение по модулю"
# )
# async def GCD(
#     response: Annotated[GCD_LCM_ABS, Depends()],
#     results: List[dict] = Depends(get_results)
# ):
#     result = reduce(gcd, response.value)
#     results.append(
#         {
#             "value": response.value,
#             "results": result
#         }
#     )
    
#     return {"success": True}

@get_rout.get(
    "/get_last",
    summary="Получить ответ на последний запрос"
)
async def get_last_answer(
    #results: List[dict] = Depends(get_results)
    ):
    try:   
        last_answer = await Request_Repository.get_last()
    except NoResultFound:  
        return {"message": "No previous results"}
    return last_answer


@get_rout.get(
    "/get_all",
    summary="Просмотреть предыдущие запросы"
)
async def get_all(
    #results: List[dict] = Depends(get_results)
    ):  
    try:  
        result = await Request_Repository.get_all()  
    except NoResultFound:  
        return {"message": "No previous results"} 
    return result  
