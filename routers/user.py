from winreg import REG_RESOURCE_REQUIREMENTS_LIST
from xmlrpc.server import resolve_dotted_attribute
from fastapi import APIRouter
from config.db import cnx
from models.Modeluser import ModelUsers
from schemas.users import User
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)


user = APIRouter()

@user.get("/")
def home():
    return cnx.execute(ModelUsers.select()).fetchall()

@user.post("/users/")
def createUser(puser:User):
    newUser = {"name":puser.name,
    "email":puser.email,
    "password":f.encrypt(puser.password.encode("utf-8"))}
    result = cnx.execute(ModelUsers.insert().values(newUser))
    return cnx.execute(ModelUsers.select().where(ModelUsers.c.id == result.lastrowid)).first()

@user.get("/users/{id}")
def UserDetails(id:str):
    return cnx.execute(ModelUsers.select().where(ModelUsers.c.id == id)).first()

@user.delete("/users/{id}")
def Delete(id:int):
    result = cnx.execute(ModelUsers.delete().where(ModelUsers.c.id == id))
    return "Usuario Eliminado"    

@user.put("/users/{id}")
def Update(id:int,puser:User):
    newUser = {"name":puser.name,
    "email":puser.email,
    "password":f.encrypt(puser.password.encode("utf-8"))}
    result = cnx.execute(ModelUsers.update().values(newUser).where(ModelUsers.c.id == id))    
    return cnx.execute(ModelUsers.select().where(ModelUsers.c.id == id)).first()
