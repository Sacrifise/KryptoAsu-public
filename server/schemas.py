from pydantic import BaseModel, field_validator
from typing import List

class GreaterCommonDivisor(BaseModel):
    elements: List[int]
    
    @field_validator("elements")
    def list_crucial_condition(cls, elem):
        if len(elem) < 2:
           raise ValueError('Список должен содержать минимум два элемента.')
        for num in elem:  
            if not isinstance(num, int) or num < 0:  
                raise ValueError('Значения должны быть целыми положительными числами!')  
                
        return elem
    
    
class LeastCommonMultiple(BaseModel):
    elements: List[int]
    
    @field_validator("elements")
    def list_crucial_condition(cls, elem):
        if len(elem) < 2:
           raise ValueError('Список должен содержать минимум два элемента.')
        for num in elem:  
            if not isinstance(num, int) or num < 0:  
                raise ValueError('Значения должны быть целыми положительными числами!')  
                
        return elem
    
class ModuleСomparison(BaseModel):
    elements: List[int]
    
    @field_validator("elements")
    def list_crucial_condition(cls, elem):
        if len(elem) < 3:
           raise ValueError('Список должен содержать минимум три элемента.')
        for num in elem:  
            if not isinstance(num, int) or num < 0:  
                raise ValueError('Значения должны быть целыми положительными числами!')  
                
        return elem