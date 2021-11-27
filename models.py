from pydantic import EmailStr, BaseModel, Field


class Employee(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(..., gt=0)
    company: str = Field(...)
    join_date: str = Field(...)
    job_title: str = Field(...)
    gender: str = Field(...)
    salary: int = Field(..., gt=0)

    class Config:
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


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
