# 8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para
# luego imprimir por pantalla la superficie total.

import console

console.clear()

print("Ingrese la base:") 
base = float(input())
print("\nIngrese la altura:")
altura = float(input())

print(f"\nFormula >> (base * altura) / 2")
print(f"        >> ({base} * {altura}) / 2")
print(f"\nEl resultado final es: {round((base * altura) / 2, 2)} mts. cuadrados\n")
