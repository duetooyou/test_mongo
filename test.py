import asyncio
import httpx
import pytest
from asgi_lifespan import LifespanManager
from motor.motor_asyncio import AsyncIOMotorClient
from database import get_database
from main import app
from models import Employee


motor_client = AsyncIOMotorClient("mongodb://localhost:27017")
database_test = motor_client["testDB"]


def get_test_database():
    return database_test


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def test_client():
    # app.dependency_overrides[get_database] = get_test_database()
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://test") as test_client:
            yield test_client


@pytest.fixture(autouse=True, scope="module")
async def initial_employees():
    employees_data = [
        Employee(name="Kamal Carson",
                 email="egestas.rhoncus.Proin@consectetuer.co.uk",
                 age=56,
                 company="Google",
                 join_date="1999-07-30T22:26:20-07:00",
                 job_title="janitor",
                 gender="female",
                 salary=9180),
        Employee(name=" Carson",
                 email="egestas.rhoncus.Proin@consectetuer.co.uk",
                 age=56,
                 company="Twitter",
                 join_date="1999-07-30T22:26:20-07:00",
                 job_title="manager",
                 gender="male",
                 salary=5180),
        Employee(name="Kama Carson",
                 email="egesta.rhoncus.Proin@consectetuer.co.uk",
                 age=36,
                 company="Yandex",
                 join_date="1999-07-30T22:26:20-07:00",
                 job_title="janitor",
                 gender="female",
                 salary=6182),
    ]
    await database_test["employee_collection"].insert_many(
        [employees.dict(by_alias=True) for employees in employees_data]
    )
    yield employees_data
    await motor_client.drop_database("testDB")


@pytest.mark.asyncio
async def test_get_employees(test_client: httpx.AsyncClient):
    response = await test_client.get(url="/employees/")
    response.status_code == 200
    print(response.json())
