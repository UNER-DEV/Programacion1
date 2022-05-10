# 15. Que pida un año y que escriba si es bisiesto o no.
# Les recordamos que los años bisiestos son múltiplos de 4,
# pero los múltiplos de 100 no lo son,
# aunque los múltiplos de 400 sí.
# Algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

from modules.utils import *

clear()

def bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

anio = int(checkNumeroPositivo(input('Ingrese un año >> ')))

if(bisiesto(anio)):
    print(f'\nEl año {anio} es bisiesto\n')
else:
    print(f'\nEl año {anio} no es bisiesto\n')
