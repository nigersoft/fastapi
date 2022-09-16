from fastapi import FastAPI
from routers.user import user
app = FastAPI(title="My API")

app.include_router(user)

