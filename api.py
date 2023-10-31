from fastapi import FastAPI
from routes.player import router
from fastapi.middleware.cors import CORSMiddleware

CORS = [
    "http://localhost:3000",
    "http://localhost:3002"
]

app = FastAPI()

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)