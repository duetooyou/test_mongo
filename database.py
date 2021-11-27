from motor.motor_asyncio import (AsyncIOMotorClient,
                                 AsyncIOMotorDatabase)


client = AsyncIOMotorClient("mongodb://localhost:27017")
database = client.employee


def get_database() -> AsyncIOMotorDatabase:
    return database
