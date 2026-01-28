from domain.pokemon import Pokemon

def test_jolly_increases_speed_and_decreases_spatk():
    charizard_Jolly = Pokemon(
        name="Charizard",
        level=50,
        types=["Fire", "Flying"],
        base_stats={"HP": 78, "Attack": 84, "Defense": 78, "Special Attack": 109, "Special Defense": 85, "Speed": 100},
        ivs={"HP": 31, "Attack": 31, "Defense": 31, "Special Attack": 31, "Special Defense": 31, "Speed": 31},
        evs={"HP": 0, "Attack": 0, "Defense": 0, "Special Attack": 252, "Special Defense": 4, "Speed": 252},
        nature="Jolly"
    )
    stats_jolly = charizard_Jolly.calculate_stats()

    charizard_Hardy = Pokemon(
        name="Charizard",
        level=50,
        types=["Fire", "Flying"],
        base_stats={"HP": 78, "Attack": 84, "Defense": 78, "Special Attack": 109, "Special Defense": 85, "Speed": 100},
        ivs={"HP": 31, "Attack": 31, "Defense": 31, "Special Attack": 31, "Special Defense": 31, "Speed": 31},
        evs={"HP": 0, "Attack": 0, "Defense": 0, "Special Attack": 252, "Special Defense": 4, "Speed": 252},
        nature="Hardy"
    )
    stats_hardy = charizard_Hardy.calculate_stats()

    assert stats_jolly["Speed"] > stats_hardy["Speed"]
    assert stats_jolly["Special Attack"] < stats_hardy["Speed"]
