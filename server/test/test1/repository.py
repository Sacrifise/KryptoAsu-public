from database import new_session, TaskOrm
from sqlalchemy import select
from schemas import GCD_LCM_ABS
from fastapi import Depends

class Request_Repository:
    @classmethod
    async def add_one_GCD_LCM_ABS(cls, data: GCD_LCM_ABS = Depends()) -> GCD_LCM_ABS:
        async with new_session() as session:
            operations_dict = data.model_dump()
            operation = TaskOrm(**operations_dict)
            session.add(operation)
            await session.flush()
            await session.commit()
            return operation
        
    # @classmethod
    # async def add_one_ABS(cls, data: ABS_crypto) -> int:
    #     async with new_session() as session:
    #         operations_dict = data.model_dump()  
    #         operation = TaskOrm(**operations_dict)
    #         session.add(operation)
    #         await session.flush()
    #         await session.commit()
    #         return operation.id
        
    @classmethod  
    async def get_all(cls):  
        async with new_session() as session:  
            query = select(TaskOrm)  
            result = await session.execute(query)  
            operations = result.scalars().all()  # Получаем все записи из базы данных
            try:
                operation_db = [GCD_LCM_ABS.model_validate(operations) for operations in operations]
            except Exception as e: 
                    print(f"Ошибка валидации записи: {operation_db}")
                    return {"success": False}  
            return operation_db  

            
     
    @classmethod
    async def get_last(cls):
        async with new_session() as session:
            query = select(TaskOrm)  
            result = await session.execute(query)  
            last_operation = result.scalars().one()
            try:
                last_operation = GCD_LCM_ABS.model_validate(last_operation)
            except Exception as e: 
                    print(f"Ошибка валидации записи: {last_operation}")
                    return {"success": False} 
            return last_operation
            
        