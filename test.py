class Cosa:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __repr__(self):
        return self.nombre


a = Cosa("nombre1")
b = Cosa("nombre2")
c = Cosa("nombre3")

lista = [a, b, c]

print(lista)
