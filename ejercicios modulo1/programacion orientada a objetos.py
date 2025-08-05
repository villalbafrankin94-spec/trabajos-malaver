# poo.py
class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def _init_(self, nombre, edad, carrera):
        super()._init_(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} estudia {self.carrera}."

p = Estudiante("Frankyn", 30, "Python")
print(p.saludar())
print(p.estudiar())
