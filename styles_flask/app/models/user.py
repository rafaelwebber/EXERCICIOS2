from pydantic import BaseModel

class LoginPayload(BaseModel):
    username:str
    password:str

class User(BaseModel):
    username: str
    lastname:str
    age: int
    email: str
    address:str


class UserDBMondel(User):
    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        if self.id:
            data['_id'] = str(data['_id'])
        return data