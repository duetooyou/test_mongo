from fastapi import FastAPI, APIRouter
from database import employee_collection
from router import router_employees


app = FastAPI(title='SimpleAPI')
app.router.include_router(router_employees)
