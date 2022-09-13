from fastapi import APIRouter
from config.db import cnx
from models.Modeluser import users
from schemas.users import User

user = APIRouter()

@user.get("/")
def home():
    return cnx.execute(users.select()).fetchall()

@user.post("/users/")
def createUser(user:User):
    return "El usuario  se creo correctamente"

@user.get("/users/id")
def Update():
    return "Pagina Principal"    
