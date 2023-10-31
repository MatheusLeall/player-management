from fastapi import APIRouter
from config.database import conn
from models.player import Player

router = APIRouter()

@router.get("/")
async def index():
    return "Welcome to full stack FARM"

@router.get("/players")
async def players_list():
    """This route returns all players registered

    Returns:
        [{
            "player_name": "John Doe",
            "player_age": 18,
            "player_team": "Real Madrid"
        }]
    """
    return conn.local.player.find()
