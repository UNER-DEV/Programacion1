from modules.utils import *

clear()

def getPromedio(num1,num2,num3):
    return float(round((num1+num2+num3)/3, 2))

num1 = float(input('Ingrese el 1er numero >> '))
num2 = float(input('Ingrese el 2do numero >> '))
num3 = float(input('Ingrese el 3er numero >> '))

print(f'\nEl promedio de los numeros ingresados es >> {getPromedio(num1,num2,num3)}\n')