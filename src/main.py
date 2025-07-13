
from fastapi import FastAPI, Form
from routes.data import data_router
from routes.base import base_router
from models import init_db

app = FastAPI()

@app.on_event("startup")
def initialise_database():
    init_db()

app.include_router(data_router)
app.include_router(base_router)