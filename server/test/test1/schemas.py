from pydantic import BaseModel, validator  
from typing import List  

class GCD_LCM(BaseModel):  
    value: List[int]  

    @validator('value')  
    def list_validator(cls, val):  
        if len(val) < 2:  
            raise ValueError('Список должен содержать минимум два элемента.')  
        return val
    
# class STaskAdd(BaseModel):
#     name: str
#     description: Optional[str] = None
    
# class STask(STaskAdd):
#     id: int