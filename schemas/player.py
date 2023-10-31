from typing import List


def player_entity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["player_name"],
        "age": db_item["player_age"],
        "team": db_item["player_team"]
    }

def player_list_schema(db_items) -> List[dict]:
    result = []
    for item in db_items:
        result.append(player_entity(item))

    return result