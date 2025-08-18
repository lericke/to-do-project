from typing import Union
from fastapi import FastAPI
from api import routers_user


app = FastAPI()

app.include_router(routers_user.router)

@app.get("/")
def root():
    return {"message": "API rodando!"}