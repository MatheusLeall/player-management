from typing import List


def player_schema(db_query) -> dict:
    return {
        "id": str(db_query["_id"]),
        "name": db_query["player_name"],
        "age": db_query["player_age"],
        "team": db_query["player_team"]
    }

def player_list_schema(db_query) -> List[dict]:
    result = []
    for item in db_query:
        result.append(player_schema(item))

    return result