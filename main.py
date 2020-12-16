from fastapi import FastAPI, HTTPException
from db.user_db import UserInDB
from db.user_db import database_users
from db.user_db import update_user, get_user
from models.user_models import UserIn, UserOut
from fastapi.middleware.cors import CORSMiddleware


origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "https://billetera-app.herokuapp.com",
]
api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

billetera_app = FastAPI()

@billetera_app.get("/user/{username}")
async def get_data(username: str):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out

@billetera_app.post("/add/usuario")
async def post_usuario(new_user:UserInDB, username:str):

    apodo = get_user(username)

    if apodo != new_user.username:
        database_users[new_user.username]=new_user
        return new_user

 