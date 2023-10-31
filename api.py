from fastapi import FastAPI
from routes.player import router

app = FastAPI()

app.include_router(router)