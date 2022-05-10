# 16. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.
# Se debe validar que el usuario ingrese sólo un carácter.
# Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato

from modules.utils import *

clear()

vocals = 'aeiou'

while True:
   print('\n\tAsegurese de que la letra sea solo de un caracter\n')
   letra = str(input('Ingrese letra >> '))
   if(len(letra) == 1):
       break

if(normalizar(letra) in vocals):
    print(f'\n\t[{letra}] Es vocal\n')
else:
    print(f'\n\t[{letra}] No es vocal\n')
