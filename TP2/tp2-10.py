# 10. Que reciba como parámetro un número y
# retorne “TRUE” si el número es par ó “FALSE” si es impar.


from modules.utils import *

clear()

def parOimpar(num):
    return num%2==0

num = int(input('Ingrese un numero >> '))

if(parOimpar(num)):
    print(f'\nEl numero ingresado [{num}] retorna [{parOimpar(num)}], es Par \n')
else:
    print(f'\nEl numero ingresado [{num}] retorna [{parOimpar(num)}], es Impar \n')