# 9. Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH

from modules.utils import *

clear()

msg = "Ingrese un mensaje >> "

msg += str(input(msg))

print(f"\t\t      {msg[::-1].replace('>','<')}\n")
