import math
from data.type_chart import get_type_multiplier


def calculate_dmg(attacker, defender, move, field=None):
    """
    Docstring para calculate_dmg
    
    attacker: Pokemon
    defender: Pokemon
    move: Move
    field: Field
    """

    level = attacker.level
    power = move.power

    if move.category == "Physical":
        Atk_stat = attacker.stats["Attack"]
        Def_stat = defender.stats["Defense"]
    else:
        Atk_stat = attacker.stats["Special Attack"]
        Def_stat = defender.stats["Special Defense"]

    #Primero - Fórmula básica de daño:
    base_dmg = (((0.2 * level + 1) * power * Atk_stat) / (Def_stat * 25) ) + 2

    #Segundo - Check STAB
    if move.type_ in attacker.types:
        stab = 1.5
    else:
        stab = 1.0

    #Tercero - Multiplicadores
    efectiveness = get_type_multiplier(move.type_, defender.types)
    multiplier = stab*efectiveness
    
    #Cuarto - Cálculo de dmg final    
    final_damage = int(base_dmg*multiplier)

    #Quinto - Cálculo de rolls
    rolls = []

    for variation in range(85,101):
        damage_roll = math.floor(final_damage * variation/100)
        rolls.append(damage_roll)
    
    return rolls