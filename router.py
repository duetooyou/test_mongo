from fastapi import APIRouter
from database import employee_collection
from models import ResponseModel, Employee, ErrorResponseModel


router_employees = APIRouter(prefix="/employees",
                             tags=["employees"])


@router_employees.get('/')
async def get_some_info():
    employees_result = []
    async for employee in employee_collection.find():
        employees_result.append(Employee(**employee))
    if employees_result:
        return ResponseModel(employees_result, "AllRight")
    return ErrorResponseModel(employees_result, '404', 'Empty')
