def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    a = validate_ingredients(ingredients)
    if "VALID" in a:
        return f"Spell recorded: {spell_name} ({a})"
    else:
        return f"Spell rejected: {spell_name} ({a})"
