class Pokemon:
    
    def __init__(self, name, level, types, base_stats, ivs, evs, nature):
        """
        Clase "Pokémon"

        Todo lo referente a datos numéricos internos del Pokémon

        Name: str -> nombre del Pokemon
        Level: int -> nivel del Pokemon
        Types: list[str] -> Lista de tipos (ej: ["Fire"])
        Base_stats: dict -> Estadísticas base, ej: {"HP": 80, "Attack": 50, ...}
        Ivs: dict -> Genes (ivs), ej: {"HP": 31, "Attack": 23, ...}
        Evs: dict -> Puntos de Esfuerzo (evs), {"HP": 180, "Attack": 252, ...}
        Nature: dict -> Multiplicadores de stats por naturaleza: {"Attack": 1.1, "Defense": 0.9, ...}
        Stats: dict -> Estadísticas finales, ej: {"HP": 180, "Attack": 154, ...}
        """
        self.name = name
        self.level = level
        self.types = types
        self.base_stats = base_stats
        self.ivs = ivs
        self.evs = evs
        self.nature = nature
        self.stats = self.calculate_stats()
    
    def calculate_stats(self):
        stats = {}
        # HP, se calcula diferente al resto de stats
        stats["HP"] = int(((2 * self.base_stats["HP"] + self.ivs["HP"] + self.evs["HP"] // 4) * self.level) // 100 + self.level + 10)
        # Otros stats
        for stat in ["Attack", "Defense", "Special Attack", "Special Defense", "Speed"]:
            stats[stat] = int((((2 * self.base_stats[stat] + self.ivs[stat] + self.evs[stat] // 4) * self.level) // 100 + 5) * self.nature.get(stat, 1))
        return stats