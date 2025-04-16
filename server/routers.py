from fastapi import APIRouter, Depends
import schemas
from functools import reduce
from math import gcd, lcm
from functions import solve_congruence
import cifers

router = APIRouter(
    prefix='/operations',
    tags=["operations"]
)

@router.post(
    "/gcd",
    summary="нод"
)
async def greater_common_divisor(
    response: schemas.GreaterCommonDivisor
):
    result = reduce(gcd, response.elements)
    return {
        "success": True,
        "type": "НОД",
        "value": response.elements,
        "result": result
    }
  
@router.post(
    "/lcm",
    summary="нок"
)
async def least_common_multiple(
    response: schemas.LeastCommonMultiple
):
    result = reduce(lcm, response.elements)
    return {
        "success": True,
        "type": "НОК",
        "value": response.elements,
        "result": result
    }
    
@router.post(
    "/module",
    summary="модуль"
)
async def module_comprasion(
    response: schemas.ModuleСomparison
):
    result = solve_congruence(response.elements)
    if result is None:
        return {
            "success": True,
            "type": "Модуль",
            "value": response.elements,
            "result": "Решений нет"
        }
    else:
        return {
            "success": True,
            "type": "Модуль",
            "value": response.elements,
            "result": result
        }
        
        
@router.post(
    "/cifers/atbash",
    summary="атбаш"
)
async def cifer_atbash(
    response: schemas.AtbashCifer
):
    answer = cifers.atbash_cifer(response.text)
    if response.operation == "encryption":
        return {
            "success": True,
            "type": "Атбаш",
            "operation": "Шифровка",
            "value": response.text,
            "result": answer
        }
    elif response.operation == "decryption":
        return {
            "success": True,
            "type": "Атбаш",
            "operation": "Дешифровка",
            "value": response.text,
            "result": answer
        }
        
@router.post(
    "/cifers/caesar",
    summary="цезарь"
)
async def cifer_caesar(
    response: schemas.CaesarCifer
):
    answer = cifers.caesar_cifer(response.text, response.shift )
    
    if response.operation == "encryption":
        return {
            "success": True,
            "type": "Цезарь",
            "operation": "Шифровка",
            "shift": response.shift,
            "value": response.text,
            "result": answer
        }
    elif response.operation == "decryption":
        return {
            "success": True,
            "type": "Цезарь",
            "operation": "Дешифровка",
            "shift": response.shift,
            "value": response.text,
            "result": answer
        }
        
@router.post(
    "/cifers/polybius",
    summary="полибий"
)
async def cifer_atbash(
    response: schemas.PolybiusCifer
):
    
    if response.operation == "encryption":
        answer = cifers.encrypt_polybius_cipher(response.text)
        return {
            "success": True,
            "type": "Полибий",
            "operation": "Шифровка",
            "value": response.text,
            "result": answer
        }
    elif response.operation == "decryption":
        answer = cifers.decrypt_polybius_cipher(response.text)
        return {
            "success": True,
            "type": "Полибий",
            "operation": "Дешифровка",
            "value": response.text,
            "result": answer
        }

