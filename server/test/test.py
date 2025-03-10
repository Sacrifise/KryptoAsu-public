from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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
    a_value: int
    b_value: int


@app.post(
    "/Operations/GCD",
    tags=["Operations"],
    summary="НОД"
)
def GCD(response: GCD_LCM):
    a = response.a_value
    b = response.b_value
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    results.append({
        "results": a if a != 0 else b,
        "a_value": response.a_value,
        "b_value": response.b_value
    })
    
    return {"succsess": True}


@app.post(
    "/Operations/LCM",
    tags=["Operations"],
    summary="НОК"
)
def LCM(response: GCD_LCM):
    a = response.a_value
    b = response.b_value
   
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    results.append({
        "results": m // (a + b),
        "a_value": response.a_value,
        "b_value": response.b_value
    })
    if len(results) > 2:
        results.pop(0)
    return {"succsess": True}


# @app.get(
#     "/GET",
#     tags=["GET_requests"],
#     summary="Получить ответ на последний запрос"
# )
# def get_last_answer():
#     return results[-1] if results else {"message": "No results yet"}


@app.get(
    "/GET/previous",
    tags=["GET_requests"],
    summary="Просмотреть предыдущие запрос"
)
def get_previous():
    return results if len(results) > 1 else {"message": "No previous results"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
