# 14. Que resuelva el siguiente problema:
# los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N
# y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla el grupo que le corresponde.

from operator import indexOf
from modules.utils import *
import string

clear()

alfabeto = string.ascii_lowercase
alfabetoParte1 = alfabeto[:indexOf(alfabeto,'m')+1]
alfabetoParte2 = alfabeto[indexOf(alfabeto,'n'):len(alfabeto)]

nombre = normalizar(str(input('Ingrese el nombre del alumno/a >> ')))

sexo = checkInputSexo('\nIngrese el sexo del alumno/a >> ')

inicial = nombre[0]

if((inicial in alfabetoParte1 and sexo == 'f') or (inicial in alfabetoParte2 and sexo == 'm')):
    print('\nEl grupo que le corresponde es el A\n')
else:
    print('\nEl grupo que le corresponde es el B\n')
