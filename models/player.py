from pydantic import BaseModel

class Player(BaseModel):
    player_name: str
    player_age: int
    player_team: str