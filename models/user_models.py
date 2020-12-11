from pydantic import BaseModel

class UserIn(BaseModel):
    nombre: str
    username: str
    password: str
    email: str

class UserOut(BaseModel):
    nombre: str
    username: str
    password: str
    email: str