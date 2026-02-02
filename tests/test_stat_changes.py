from domain.pokemon import Pokemon
from domain.move import Move
from domain.dmg_calc import calculate_dmg

def test_jolly_increases_speed_and_decreases_spatk():
    charizard = Pokemon(
        name="Charizard",
        level=50,
        types=["Fire", "Flying"],
        base_stats={"HP": 78, "Attack": 84, "Defense": 78, "Special Attack": 109, "Special Defense": 85, "Speed": 100},
        ivs={"HP": 31, "Attack": 31, "Defense": 31, "Special Attack": 31, "Special Defense": 31, "Speed": 31},
        evs={"HP": 0, "Attack": 0, "Defense": 0, "Special Attack": 252, "Special Defense": 4, "Speed": 252},
        nature="Jolly"
    )
    
    venusaur = Pokemon(
        name="Venusaur",
        level=50,
        types=["Grass", "Poison"],
        base_stats={"HP": 80, "Attack": 82, "Defense": 83, "Special Attack": 100, "Special Defense": 100, "Speed": 80},
        ivs={"HP": 31, "Attack": 31, "Defense": 31, "Special Attack": 31, "Special Defense": 31, "Speed": 31},
        evs={"HP": 252, "Attack": 0, "Defense": 4, "Special Attack": 252, "Special Defense": 0, "Speed": 0},
        nature="Modest"
    )

    flamethrower = Move(name="Flamethrower", type_="Fire", category="Special", power=90)

    damage_sin_boost = calculate_dmg(charizard, venusaur, flamethrower)

    charizard_sin_boost = charizard.calculate_stats()
    venusaur_sin_boost = venusaur.calculate_stats()
    charizard.stat_changes["Special Attack"] = 2
    venusaur.stat_changes["Special Defense"] = -2
    damage_con_boost = calculate_dmg(charizard, venusaur, flamethrower)

    assert charizard_sin_boost["Special Attack"] < charizard.get_modified_stat("Special Attack")
    assert venusaur_sin_boost["Special Defense"] > venusaur.get_modified_stat("Special Defense")
    assert damage_sin_boost < damage_con_boost
