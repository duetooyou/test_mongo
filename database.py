from motor import motor_asyncio


client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.employee
employee_collection = db.get_collection("employee_collection")
