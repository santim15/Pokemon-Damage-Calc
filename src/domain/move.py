class Move:
    
    def __init__(self, name, type_, category, power):
        """
        Clase "Move"

        Todo lo referente a datos numéricos internos del movimiento

        Name: str -> nombre del Pokemon
        Type_: list[str] -> Lista de tipos (ej: ["Fire"])
        Category: str -> "Physical" o "Special"
        Power: int -> Potencia base del movimiento
        """
        self.name = name
        self.type_ = type_
        self.category = category
        self.power = power