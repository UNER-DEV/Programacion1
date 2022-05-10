from modules.utils import *

clear()

def repetirPalabra(palabra,cantidadVeces=10):
    return palabra*cantidadVeces

palabra = str(input('Ingrese una palabra >> '))

print('\nLa siguiente se repetira 10 veces:')
print(repetirPalabra(f'{palabra}\n'))
