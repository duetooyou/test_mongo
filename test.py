import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from starlette.responses import PlainTextResponse
from main import app as my_app


@pytest.fixture
async def app():
    async def startup():
        print("Starting up")

    async def shutdown():
        print("Shutting down")

    async def home(request):
        return PlainTextResponse("Hello, world!")

    app = my_app

    async with LifespanManager(app):
        print("We're in!")
        yield app


@pytest.fixture
async def client(app):
    async with AsyncClient(app=my_app) as client:
        print("Client is ready")
        yield client


@pytest.mark.anyio()
async def test_get_all_employees(client):
    print("OK")
