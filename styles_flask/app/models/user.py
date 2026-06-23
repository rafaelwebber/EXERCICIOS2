from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field, SecretStr

class LoginPayload(BaseModel):
    username:str
    password:str

class UserCreate(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    username: str
    lastname:str
    password:SecretStr
    age: int
    email: str
    address:str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class UserPublic(BaseModel):
    id:Optional[ObjectId] = Field(None, alias="_id")
    username: str
    lastname: str
    age: int
    email: str
    address: str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )