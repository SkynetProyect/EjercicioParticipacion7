from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other) -> bool:
        if self.nombre == other.nomre:
            return True
        else:
            return False

    def __repr__(self):
        return self.nombre


class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        Conjunto.contador += 1

        self.lista: list[Elemento] = []
        self.nombre = nombre
        self.__id: int = Conjunto.contador

    def contiene(self, objeto: Elemento):
        if objeto not in self.lista:
            return True
        else:
            return False

    def agregar_elemento(self, objeto: Elemento):
        if self.contiene(objeto):
            self.lista.append(objeto)

    def __iadd__(self, other):
        self.lista = self.lista + other.lista

    def unir(self, other):
        self.lista = self.lista + other.lista

    def __str__(self):

        return f"Conjunto {self.nombre}:: {self.lista}"
