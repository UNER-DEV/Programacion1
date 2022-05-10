from modules.utils import *

clear()

contador = 0

for i in range(0,101):
    if(esPrimo(i)):
        print(i, end = ' ')
        contador += 1

print(f'\n\nEntre el 0 y 100, existen {contador} numeros primos\n')    
