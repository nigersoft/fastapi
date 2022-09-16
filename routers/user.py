
from fastapi import APIRouter, status
from config.db import cnx
from models.Modeluser import ModelUsers
from schemas.users import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)


user = APIRouter()

@user.get("/",response_model=list[User], tags=["Users"])
def home():
    return cnx.execute(ModelUsers.select()).fetchall()

@user.post("/users/",response_model=User, tags=["Users"])
def createUser(puser:User):
    newUser = {"name":puser.name,
    "email":puser.email,
    "password":f.encrypt(puser.password.encode("utf-8"))}
    result = cnx.execute(ModelUsers.insert().values(newUser))
    return cnx.execute(ModelUsers.select().where(ModelUsers.c.id == result.lastrowid)).first()

@user.get("/users/{id}", response_model= User, tags=["Users"])
def UserDetails(id:str):
    return cnx.execute(ModelUsers.select().where(ModelUsers.c.id == id)).first()

@user.delete("/users/{id}",status_code=status.HTTP_200_OK, tags=["Users"])
def Delete(id:int):
    result = cnx.execute(ModelUsers.delete().where(ModelUsers.c.id == id))
    return "Usuario Eliminado"    

@user.put("/users/{id}",response_model=User, tags=["Users"])
def Update(id:int,puser:User):
    newUser = {"name":puser.name,
    "email":puser.email,
    "password":f.encrypt(puser.password.encode("utf-8"))}
    result = cnx.execute(ModelUsers.update().values(newUser).where(ModelUsers.c.id == id))    
    
    return cnx.execute(ModelUsers.select().where(ModelUsers.c.id == id)).first()
