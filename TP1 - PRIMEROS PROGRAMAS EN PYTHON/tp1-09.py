# INTEGRANTES:
    # Camila Laureana Silva
    # Federico José Rodriguez
    # María Emilia Walter
    # Sebastian Ignacio Centurion

# 9. Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH

import console

console.clear()

msg = "Ingrese un mensaje >> "

msg += str(input(msg))

print(f"\t\t      {msg[::-1].replace('>','<')}\n")
