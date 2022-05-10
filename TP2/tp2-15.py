from modules.utils import *

clear()

def bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

anio = int(checkNumeroPositivo(input('Ingrese un año >> ')))

if(bisiesto(anio)):
    print(f'\nEl año {anio} es bisiesto\n')
else:
    print(f'\nEl año {anio} no es bisiesto\n')
