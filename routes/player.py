from fastapi import APIRouter
from config.database import conn
from models.player import Player

router = APIRouter()

@router.get("/")
async def index():
    return "Welcome to full stack FARM"
