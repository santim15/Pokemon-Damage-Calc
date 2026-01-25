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

    #Tercero - Cálculo final
    final_damage = int(base_dmg*stab)
    
    return final_damage