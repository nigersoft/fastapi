from fastapi import APIRouter

user = APIRouter()

@user.get("/")
def home():
    return "Pagina Principal"

@user.get("/users/id")
def Details():
    return "Pagina Principal"

@user.get("/users/id")
def Update():
    return "Pagina Principal"    
