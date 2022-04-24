# 9. Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH

import console

console.clear()

msg = str(input("Ingrese un mensaje: "))

print(f"\t\t    {msg[::-1]}\n")