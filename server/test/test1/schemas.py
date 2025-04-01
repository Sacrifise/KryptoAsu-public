from pydantic import BaseModel, field_validator 
from typing import List  

class GCD_LCM_ABS(BaseModel):  
    value: List[int]  

    @field_validator('value')  
    def validate(cls, val):  
        if len(val) < 2:  
            raise ValueError('Список должен содержать минимум два элемента.')
        for num in val:  
            if not isinstance(num, int) or num < 0:  
                raise ValueError('Значения должны быть целыми положительными числами!')  
                
        return val  
    
# class ABS_crypto(BaseModel):
#     value_a: int
#     value_b: int
#     value_n: int
    
#     @field_validator('value_a', 'value_b', 'value_n')  
#     def validate(cls, value):  
#         if not isinstance(value, int):  
#             raise ValueError('Значение должно быть целым числом.')  
#         if value <= 0:  
#             raise ValueError('Значение должно быть положительным.')  
#         return value
    