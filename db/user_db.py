from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    nombre: str
    username: str
    password: str
    email: str

database_users = Dict[str, UserInDB]

database_users = {
    "alejo14": UserInDB(**{"nombre":"Alejandro Pelaez","username":"alejo14",
                            "password":"root","email":"alejandro@gmail.com",
                            }),
    
    "yeimi12": UserInDB(**{"nombre":"Angelica Quintero","username":"yeimi12",
                            "password":"root","email":"angelica@gmail.com",
                            }),

    "juanjo08": UserInDB(**{"nombre":"Daniela Londoño ","username":"juanjo08",
                            "password":"root","email":"angie@gmail.com",
                            }),
    
    "domimorte04": UserInDB(**{"nombre":"David Diaz","username":"domimorte04",
                            "password":"root","email":"david@gmail.com",
                            }),

    "sebas": UserInDB(**{"nombre":"Sebastian Vasquez","username":"sebas",
                            "password":"root","email":"juanse@gmail.com",
                            }),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def post_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db.username


def update_user (user_in:dict):
    if isinstance(database_users[user_in["username"]], UserInDB):
        new_user = database_users[user_in["username"]].dict()
    else: new_user = database_users[user_in["username"]]
    for key in user_in:
        new_user[key] = user_in[key]
    database_users[user_in["username"]]=new_user
    print(database_users[user_in["username"]])
    return user_in["username"]
        

