from fastapi import FastAPI
from router import router_employees

app = FastAPI(title='SimpleAPI')
app.router.include_router(router_employees)


@app.on_event("startup")
async def startup():
    print("Старт")


@app.on_event("shutdown")
async def shutdown():
    print("Стоп")
