from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, validator  
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from functools import reduce
from math import gcd, lcm


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
    "http://192.168.0.106:5173/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

results = []


class GCD_LCM(BaseModel):  
    value: List[int]  

    @validator('value')  
    def list_validator(cls, val):  
        if len(val) < 2:  
            raise ValueError('Список должен содержать минимум два элемента.')  
        return val

class ABS_crypto(BaseModel):
    value_a: int
    value_b: int
    value_n: int
    
def extended_gcd(a, b):
    """Расширенный алгоритм Евклида для нахождения НОД и коэффициентов Безу."""
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def modular_inverse(a, m):
    """Находит обратный элемент к a по модулю m, если он существует."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None  # Обратный элемент не существует, если a и m не взаимно просты
    else:
        return x % m

def solve_congruence(a, b, m):
    """Решает уравнение сравнения a*x ≡ b (mod m)."""
    d = gcd(a, m)
    if b % d != 0:
        return None  # Решений нет, если b не делится на d
    a_reduced = a // d
    b_reduced = b // d
    m_reduced = m // d

    # Находим обратный элемент к a_reduced по модулю m_reduced
    inv = modular_inverse(a_reduced, m_reduced)
    if inv is None:
        return None  # Обратный элемент не существует

    # Находим одно из решений
    x0 = (inv * b_reduced) % m_reduced

    # Все решения по модулю m
    solutions = [(x0 + k * m_reduced) % m for k in range(d)]
    return solutions

@app.post(
    "/Operations/ABS",
    tags=["Operations"],
    summary="Модуль"
)
def GCD(response: ABS_crypto):
    result = solve_congruence(response.value_a, response.value_b, response.value_n)
    if result is None:
        result = "Решений нет"
    else:
        result = f"Решения уравнения {response.value_a}x ≡ {response.value_b} (mod {response.value_n}): {result}"
    results.append(
        {
            "value_a": response.value_a,
            "value_b": response.value_b,
            "value_n": response.value_n,
            "results": result
            
        }
    )
    
    return {"succsess": True}

@app.post(
    "/Operations/GCD",
    tags=["Operations"],
    summary="НОД"
)
def GCD(response: GCD_LCM):
    result = reduce(gcd, response.value)
    results.append(
        {
            "value": response.value,
            "results": result
            
        }
    )
    
    return {"succsess": True}


@app.post(
    "/Operations/LCM",
    tags=["Operations"],
    summary="НОК"
)
def LCM(response: GCD_LCM):
    result = reduce(lcm, response.value)
    results.append(
        {
            "value": response.value,
            "results": result
            
        }
    )
    return {"succsess": True}


@app.get(
    "/GET",
    tags=["GET_requests"],
    summary="Получить ответ на последний запрос"
)
def get_last_answer():
    return results[-1] if results else {"message": "No results yet"}


@app.get(
    "/GET/previous",
    tags=["GET_requests"],
    summary="Просмотреть предыдущие запрос"
)
def get_previous():
    return results if len(results) > 1 else {"message": "No previous results"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


