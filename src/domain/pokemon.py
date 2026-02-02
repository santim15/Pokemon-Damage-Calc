from data.natures import NATURES
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
        Stat_changes: dict -> Aumentos o detrimentos en las estadisticas
        """
        self.name = name
        self.level = level
        self.types = types
        self.base_stats = base_stats
        self.ivs = ivs
        self.evs = evs
        self.nature = nature
        self.stats = self.calculate_stats()
        self.stat_changes = {
            "Attack": 0,
            "Defense": 0,
            "Special Attack": 0,
            "Special Defense": 0,
            "Speed": 0
        }

    
    def get_stage_multiplier(self, change):
        #Transforma +1 -> x1.5, +2 -> x2, -1 -> x2/3, -2 -> x0.5...
        if change >= 0:
            return (2 + change) / 2
        else:
            return 2 / (2 - change)

    def get_modified_stat(self, stat_name):
        base_stat = self.stats[stat_name]
        changes = self.stat_changes.get(stat_name, 0)
        multiplier = self.get_stage_multiplier(changes)
        return base_stat * multiplier


    def calculate_stats(self):
        stats = {}
        # HP, se calcula diferente al resto de stats
        stats["HP"] = int(((2 * self.base_stats["HP"] + self.ivs["HP"] + self.evs["HP"] // 4) * self.level) // 100 + self.level + 10)

        nature_data = NATURES.get(self.nature,None)
        # Otros stats
        for stat in ["Attack", "Defense", "Special Attack", "Special Defense", "Speed"]:
            base_value = int(((2 * self.base_stats[stat] + self.ivs[stat] + self.evs[stat] // 4) * self.level) // 100 + 5) 
            nat_modifier = 1
            if nature_data:
                if stat == nature_data["increase"]:
                    nat_modifier = 1.1
                elif stat == nature_data["decrease"]:
                    nat_modifier = 0.9

            stats[stat] = int(base_value * nat_modifier)

        return stats