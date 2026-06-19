from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field

class LoginPayload(BaseModel):
    username:str
    password:str

class User(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    username: str
    lastname:str
    age: int
    email: str
    address:str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )


class UserDBMondel(User):
    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        if self.id:
            data['_id'] = str(data['_id'])
        return data