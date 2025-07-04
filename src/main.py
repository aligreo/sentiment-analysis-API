from fastapi import FastAPI
from routes.process_data import data_router
from routes.base import base_router

app = FastAPI()
app.include_router(data_router)
app.include_router(base_router)