from fastapi import APIRouter
from config.database import conn
from models.player import Player
from schemas.player import player_schema, player_list_schema
from bson import ObjectId

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

@router.get("/players/{player_id}")
def get_player(player_id):
    """This route implements a GET method to obtain a specific player

    Args:
        player_id (UUId)

    Returns:
        [{
            "player_name": "John Doe",
            "player_age": 18,
            "player_team": "Real Madrid"
        }]
    """

    player_result = conn.local.player.find_one(
        {
            "_id": ObjectId(player_id)
        }
    )

    return player_schema(player_result)

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

@router.put("/players/{player_id}")
async def update_player(player_id, player: Player):
    """_summary_

    Args:
        player_id (UUID)
        player (Player)

    Returns:
        [{
            "player_name": "John Doe",
            "player_age": 18,
            "player_team": "Real Madrid"
        }]
    """

    player_update_information = dict(player)
    conn.local.player.find_one_and_update({"_id": ObjectId(player_id)}, {"$set": player_update_information})
    return player_schema(conn.local.player.find_one({"_id": ObjectId(player_id)}))