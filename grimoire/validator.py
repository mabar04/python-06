def validate_ingredients(ingredients: str) -> str:
    if "fire" or "water" or "earth" or "air" in ingredients:
        return f"{ingredients} VALID"
    else:
        return f"{ingredients} INVALID"
