from data.type_chart import get_type_multiplier

def test_fire_vs_grass():
    assert get_type_multiplier("Fire", ["Grass"]) == 2.0

def test_fire_vs_water():
    assert get_type_multiplier("Fire", ["Water"]) == 0.5

def test_fire_vs_grass_steel():
    assert get_type_multiplier("Fire", ["Grass", "Steel"]) == 4.0
