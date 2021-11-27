from bson import ObjectId
from pydantic import EmailStr, BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Employee(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(..., gt=0)
    company: str = Field(...)
    join_date: str = Field(...)
    job_title: str = Field(...)
    gender: str = Field(...)
    salary: int = Field(..., gt=0)

    class Config:
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Kamal Carson",
                "email": "egestas.rhoncus.Proin@consectetuer.co.uk",
                "age": 56,
                "company": "Google",
                "join_date": "1999-07-30T22:26:20-07:00",
                "job_title": "janitor",
                "gender": "female",
                "salary": 9180
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(code, message):
    return {"code": code, "message": message}
