from fastapi import APIRouter, Query, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from database import get_database
from models import ResponseModel, Employee, ErrorResponseModel


router_employees = APIRouter(prefix="/employees",
                             tags=["employees"])


@router_employees.get('/')
async def get_all_employees(database: AsyncIOMotorDatabase = Depends(get_database),
                            company: str = Query("Google")):
    collection = database.employee_collection.find({"company": company})
    employees = [Employee(**employees) async for employees in collection]
    if employees:
        return ResponseModel(employees, 'all right')
    return ErrorResponseModel('error_code', 'smthng wrong')
