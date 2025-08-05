# funciones.py
def saludar(Frankyn):
    """Función tradicional"""
    return f"Hola {Frankyn}"

doblar = lambda x: x * 2  # Función lambda

print(saludar("Frankyn"))
print("El doble de 5 es:", doblar(5))

