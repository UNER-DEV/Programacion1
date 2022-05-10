# 8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo 
# para luego imprimir por pantalla la superficie total.

from modules.utils import *

clear()

base = float(input("Ingrese la base del triangulo >> "))
altura = float(input("Ingrese la altura del triangulo >> "))

print(f"\nFormula >> (base * altura) / 2")
print(f"        >> ({base} m * {altura} m) / 2")
print(f"\nEl resultado final es: {round((base * altura) / 2, 2)} m^2\n")
