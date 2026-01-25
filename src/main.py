from domain.pokemon import Pokemon
from domain.move import Move
from domain.dmg_calc import calculate_dmg

# Datos de ejemplo
charizard = Pokemon(
    name="Charizard",
    level=50,
    types=["Fire", "Flying"],
    base_stats={"HP": 78, "Attack": 84, "Defense": 78, "Special Attack": 109, "Special Defense": 85, "Speed": 100},
    ivs={"HP": 31, "Attack": 31, "Defense": 31, "Special Attack": 31, "Special Defense": 31, "Speed": 31},
    evs={"HP": 0, "Attack": 0, "Defense": 0, "Special Attack": 252, "Special Defense": 4, "Speed": 252},
    nature={"Attack":1, "Defense":1, "Special Attack":1.1, "Special Defense":1, "Speed":1.1}
)

venusaur = Pokemon(
    name="Venusaur",
    level=50,
    types=["Grass", "Poison"],
    base_stats={"HP": 80, "Attack": 82, "Defense": 83, "Special Attack": 100, "Special Defense": 100, "Speed": 80},
    ivs={"HP": 31, "Attack": 31, "Defense": 31, "Special Attack": 31, "Special Defense": 31, "Speed": 31},
    evs={"HP": 252, "Attack": 0, "Defense": 4, "Special Attack": 252, "Special Defense": 0, "Speed": 0},
    nature={"Attack":1, "Defense":1, "Special Attack":1.1, "Special Defense":1, "Speed":1}
)

flamethrower = Move(name="Flamethrower", type_="Fire", category="Special", power=90)

damage = calculate_dmg(charizard, venusaur, flamethrower)
print(f"Daño estimado: {damage}")
