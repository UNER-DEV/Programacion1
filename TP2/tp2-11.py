# 11. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
# a. Todos los números impares desde 1 hasta ese número separados por comas.
# b. La cuenta atrás desde ese número hasta cero separados por comas.
# c. Que indique si es primo o no.
# d. Por último, su factorial.

from modules.utils import *
import math

clear()

def contarImpares(num):
    lstImpares = []
    for i in range(1,num+1,2):
        lstImpares.append(i)
    return lstImpares

def contarAtras(num):
    lstReversa = []
    for i in range(0,num+1):
        lstReversa.append(i)
    lstReversa.reverse()
    return lstReversa

num = checkNumeroPositivo(int(input('Ingrese un numero entero positivo >> ')))

print(f'\nA continuacion mostraremos todos los numeros impares, contando desde el 1 hasta {num}')
print(contarImpares(num))

print(f'\nLuego, mostraremos un conteo hacia atras partiendo del numero hasta cero')
print(contarAtras(num))

valorPrimo = esPrimo(num)

if(valorPrimo):
    print(f'\nEl numero ingresado [{num}] retorna [{valorPrimo}], es Primo')
else:
    print(f'\nEl numero ingresado [{num}] retorna [{valorPrimo}], no es Primo')

print(f'\nPor ultimo, su factorial es: {math.factorial(num)}\n')





