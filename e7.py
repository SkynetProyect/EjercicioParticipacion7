from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other) -> bool:
        if self.nombre == other.nomre:
            return True
        else:
            return False

class Conjunto:

    def __init__(self):
        