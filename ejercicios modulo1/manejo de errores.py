# excepciones.py
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError as e:
    print("Error:", e)
except ValueError:
    print("Debes ingresar un número.")
finally:
    print("Ejecución terminada.")
