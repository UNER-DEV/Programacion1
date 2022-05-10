# 1. Que al pasarle una cadena <nombre> 
# nos muestre por pantalla el saludo ¡Hola <nombre>!

from modules.utils import *

clear()

def saludo(nombre):
    print(f'\nHola {nombre}\n')

saludo(str(input('Cual es su nombre? >> ')))