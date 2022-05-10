from modules.utils import *

clear()

base = checkNumeroPositivo(float(input('Ingrese la base del triangulo >> ')))
altura = checkNumeroPositivo(float(input('\nIngrese la altura del triangulo >> ')))

print(f'\nEl area del triangulo es de {getAreaTriangulo(base,altura)} m^2\n')