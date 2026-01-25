class Field:
    
    def __init__(self, weather=None, terrain=None, screens=None):
        """
        Clase "Field"

        Todo lo referente a variables del campo de batalla

        weather: str -> Tiempo Atmosférico ("Sunny", "Rain", ...)
        terrain: str -> Campo ("Grassy", "Electric"...)
        screens: dict -> Barreras {"Reflect": bool, "Light Screen": bool}
        """
        self.weather = weather
        self.terrain = terrain
        self.screens = screens