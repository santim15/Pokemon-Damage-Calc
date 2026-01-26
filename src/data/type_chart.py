# type_chart.py -> Multiplicadores de daño de efectividad y resistencia de los tipos elementales

TYPE_CHART = {
    "Steel": {
        "Steel": 0.5,
        "Water": 0.5,
        "Electric": 0.5,
        "Fire": 0.5,
        "Fairy": 2.0,
        "Ice": 2.0,
        "Rock": 2.0
    },
    "Water": {
        "Fire": 2.0,
        "Ground": 2.0,
        "Rock": 2.0,
        "Water": 0.5,
        "Grass": 0.5,
        "Dragon": 0.5
    },
    "Bug": {
        "Steel": 0.5,
        "Ghost": 0.5,
        "Fire": 0.5,
        "Fairy": 0.5,
        "Fighting": 0.5,
        "Grass": 2.0,
        "Psychic": 2.0,
        "Dark": 2.0,
        "Poison": 0.5,
        "Flying": 0.5
    },
    "Dragon": {
        "Steel": 0.5,
        "Dragon": 2.0,
        "Fairy": 0.0
    },
    "Electric": {
        "Water": 2.0,
        "Dragon": 0.5,
        "Electric": 0.5,
        "Grass": 0.5,
        "Ground": 0.0,
        "Flying": 2.0
    },
    "Ghost": {
        "Ghost": 2.0,
        "Normal": 0.0,
        "Psychic": 2.0,
        "Dark": 0.5
    },
    "Fire": {
        "Steel": 2.0,
        "Water": 0.5,
        "Bug": 2.0,
        "Dragon": 0.5,
        "Fire": 0.5,
        "Ice": 2.0,
        "Grass": 2.0,
        "Rock": 0.5
    },
    "Fairy": {
        "Steel": 0.5,
        "Dragon": 2.0,
        "Fire": 0.5,
        "Fighting": 2.0,
        "Dark": 2.0,
        "Poison": 0.5
    },
    "Ice": {
        "Steel": 0.5,
        "Water": 0.5,
        "Dragon": 2.0,
        "Fire": 0.5,
        "Ice": 0.5,
        "Grass": 2.0,
        "Ground": 2.0,
        "Flying": 2.0
    },
    "Fighting": {
        "Steel": 2.0,
        "Bug": 0.5,
        "Ghost": 0.0,
        "Fairy": 0.5,
        "Ice": 2.0,
        "Normal": 2.0,
        "Psychic": 0.5,
        "Rock": 2.0,
        "Dark": 2.0,
        "Poison": 0.5,
        "Flying": 0.5
    },
    "Normal": {
        "Steel": 0.5,
        "Ghost": 0.0,
        "Rock": 0.5
    },
    "Grass": {
        "Steel": 0.5,
        "Water": 2.0,
        "Bug": 0.5,
        "Dragon": 0.5,
        "Fire": 0.5,
        "Grass": 0.5,
        "Rock": 2.0,
        "Ground": 2.0,
        "Poison": 0.5,
        "Flying": 0.5
    },
    "Psychic": {
        "Steel": 0.5,
        "Fighting": 2.0,
        "Psychic": 0.5,
        "Dark": 0.0,
        "Poison": 2.0
    },
    "Rock": {
        "Steel": 0.5,
        "Bug": 2.0,
        "Fire": 2.0,
        "Ice": 2.0,
        "Fighting": 0.5,
        "Ground": 0.5,
        "Flying": 2.0
    },
    "Dark": {
        "Ghost": 2.0,
        "Fairy": 0.5,
        "Fighting": 0.5,
        "Psychic": 2.0,
        "Dark": 0.5
    },
    "Ground": {
        "Steel": 2.0,
        "Bug": 0.5,
        "Electric": 2.0,
        "Fire": 2.0,
        "Grass": 0.5,
        "Rock": 2.0,
        "Poison": 2.0,
        "Flying": 0.0
    },
    "Poison": {
        "Steel": 0.0,
        "Ghost": 0.5,
        "Fairy": 2.0,
        "Grass": 2.0,
        "Rock": 0.5,
        "Ground": 0.5,
        "Poison": 0.5
    },
    "Flying": {
        "Steel": 0.5,
        "Bug": 2.0,
        "Electric": 0.5,
        "Fighting": 2.0,
        "Grass": 2.0,
        "Rock": 0.5
    }
}

def get_type_multiplier(move_type: str, defender_types: list[str]) -> float:
    multiplier = 1.0

    for defender_type in defender_types:

        # Si el tipo defensor no está definido, asumimos 1.0 (neutro)
        type_effectiveness = TYPE_CHART[move_type].get(defender_type, 1.0)

        multiplier *= type_effectiveness

    return multiplier
