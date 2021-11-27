from fastapi import FastAPI
from router import router_employees


app = FastAPI(title='SimpleAPI')
app.router.include_router(router_employees)
