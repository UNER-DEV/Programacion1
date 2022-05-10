from modules.utils import *

clear()

def parOimpar(num):
    return num%2==0

num = int(input('Ingrese un numero >> '))

if(parOimpar(num)):
    print(f'\nEl numero ingresado [{num}] retorna [{parOimpar(num)}], es Par \n')
else:
    print(f'\nEl numero ingresado [{num}] retorna [{parOimpar(num)}], es Impar \n')