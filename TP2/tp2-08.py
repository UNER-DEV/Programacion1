from modules.utils import *

clear()

edad = int(input('Ingrese su edad >> '))

if(edad >= 18):
    print('\nEs mayor de edad\n')
elif(0 < edad < 18):
    print('\nNo es mayor de edad\n')
else:
    print('\nEdad indefinida\n')