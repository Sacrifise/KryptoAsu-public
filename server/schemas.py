from pydantic import BaseModel, field_validator, Field
from typing import List, Literal

    
class AtbashCifer(BaseModel):
    text: str
    operation: Literal["encryption", "decryption"] = Field()

    @field_validator("text")
    
    def validate_alphabet(cls, text_encryption):
        rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        eng_alph = 'abcdefghijklmnopqrstuvwxyz'
        digits = "0987654321"
        if any(c in text_encryption for c in digits):  
             raise ValueError("Текст не может содержать числа!")  

        rus_chars = any(c in rus_alph for c in text_encryption)  
        eng_chars = any(c in eng_alph for c in text_encryption)  

        if rus_chars and eng_chars:  
            raise ValueError("Текст должен содержать буквы только одного алфавита!")  
        elif not rus_chars and not eng_chars:  
            raise ValueError("Текст должен содержать буквы русского или английского алфавита!")
        
        return text_encryption

class CaesarCifer(BaseModel):
    text: str
    shift: int
    operation: Literal["encryption", "decryption"] = Field()

    @field_validator("text")
    def validate_alphabet(cls, text_encryption):
        rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        eng_alph = 'abcdefghijklmnopqrstuvwxyz'
        digits = "0987654321"
        if any(c in text_encryption for c in digits):  
             raise ValueError("Текст не может содержать числа!")  

        rus_chars = any(c in rus_alph for c in text_encryption)  
        eng_chars = any(c in eng_alph for c in text_encryption)  

        if rus_chars and eng_chars:  
            raise ValueError("Текст должен содержать буквы только одного алфавита!")  
        elif not rus_chars and not eng_chars:  
            raise ValueError("Текст должен содержать буквы русского или английского алфавита!")
        
        return text_encryption
    
class PolybiusCifer(BaseModel):
    text: str
    operation: Literal["encryption", "decryption"] = Field()

    @field_validator("text")
    def validate_alphabet(cls, text_encryption):
        rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        eng_alph = 'abcdefghijklmnopqrstuvwxyz'
        digits = "0987654321"
        
        if text_encryption.isdigit():
            return text_encryption
        
        if any(c in text_encryption for c in digits):  
             raise ValueError("Текст не может содержать числа!")  

        rus_chars = any(c in rus_alph for c in text_encryption)  
        eng_chars = any(c in eng_alph for c in text_encryption)  

        if rus_chars and eng_chars:  
            raise ValueError("Текст должен содержать буквы только одного алфавита!")  
        elif not rus_chars and not eng_chars:  
            raise ValueError("Текст должен содержать буквы русского или английского алфавита!")
        
        return text_encryption
    
class LeastCommonMultiple(BaseModel):
    elements: List[int]
    
    @field_validator("elements")
    def list_crucial_condition(cls, elem):
        if len(elem) < 2:
           raise ValueError('Для вычисления НОК необходимо минимум два элемента.')
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
    
class GreaterCommonDivisor(BaseModel):
    elements: List[int]
    
    @field_validator("elements")
    def list_crucial_condition(cls, elem):
        if len(elem) < 2:
           raise ValueError('Для вычисления НОД необходимо минимум два элемента.')
        for num in elem:  
            if not isinstance(num, int) or num < 0:  
                raise ValueError('Значения должны быть целыми положительными числами!')  
                
        return elem