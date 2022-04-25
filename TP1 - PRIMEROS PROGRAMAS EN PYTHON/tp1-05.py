# INTEGRANTES:
    # Camila Laureana Silva
    # Federico José Rodriguez
    # María Emilia Walter
    # Sebastian Ignacio Centurion

# 5. Escriba un programa que pida al usuario que ingrese 3 números. 
# Sume los dos primeros y luego multiplique este total por el tercero. 
# Mostrar la respuesta en pantalla de la siguiente forma: “La respuesta es XX”.

import console

console.clear()

num1 = int(input("Ingrese el 1er numero  >>  "))
num2 = int(input("Ingrese el 2do numero  >>  "))
num3 = int(input("Ingrese el 3er numero  >>  "))
print(f"\nLA RESPUESTA ES >> ({num1} + {num2}) * {num3} = {(num1 + num2) * num3}\n")
