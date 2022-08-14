from fastapi import FastAPI

from .routers import login, register

app = FastAPI()

# app.include_router(login.router)
# app.include_router(register.router)

from app.models import connect

@app.get("/")
async def root():
    return {"Hello": "World"}