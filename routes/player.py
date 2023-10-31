from fastapi import APIRouter
from config.database import conn
from models.player import Player
from schemas.player import player_schema, player_list_schema

router = APIRouter()

@router.get("/")
async def index():
    return "Welcome to full stack FARM"

@router.get("/players")
async def list_players():
    """This route returns all players registered

    Returns:
        [{
            "player_name": "John Doe",
            "player_age": 18,
            "player_team": "Real Madrid"
        }]
    """
    return player_list_schema(conn.local.player.find())

@router.post("/players")
async def create_player(player: Player):
    """This route implements the POST method to create new players

    Args:
        player (Player)

    Returns:
        [{
            "player_name": "John Doe",
            "player_age": 18,
            "player_team": "Real Madrid"
        },
        {
            "player_name": "John Moore",
            "player_age": 19,
            "player_team": "Manchester United"
        }]
    """

    player_to_insert = dict(player)
    conn.local.player.insert_one(player_to_insert)
    return player_list_schema(conn.local.player.find())
