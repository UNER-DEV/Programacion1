# 5.Escriba un programa Python que solicite al usuario el ingreso de números enteros. 
# Cuando el usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. 
#  Cada uno de los números ingresados por el usuario deberá ser almacenado en una lista.
#  A continuación, realice las siguientes tareas:
    # a. Determinar el máximo.
    # b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
    # c. Determinar el mínimo.
    # d. Calcular la multiplicación de  todos los números de la lista.
    # e. Contar los valores pares e impares.
    # f. Remover los elementos repetidos

from modules.utils import *
from collections import OrderedDict

clear()

lista_enteros=[]

print('A continuación deberá ingresar un n° y podrá hacerlo las veces que quiera.\nPara finalizar escriba la palabra "fin".')
while True:
    entero=normalizar(input('\n\nIngrese un número entero o escriba "fin" >> '))
    clear()
    if(entero == 'fin'):
        break
    elif(checkNumero(entero)):
        lista_enteros.append(int(entero))
        print(f"Se ha agregado correctamente el número {entero}")
     
lista_enteros = sorted(lista_enteros)

sin_repetidos = list(OrderedDict.fromkeys(lista_enteros))
# otra opc => sin_repetidos = quitarRepetidos(lista_enteros)

print(f"\n >> Todos los números ingresados son {lista_enteros}\n")

print(f' >> El número más alto de esa lista es {max(sin_repetidos)}, el segundo número más alto es {sin_repetidos[-2]} y el número más bajo es {min(sin_repetidos)}.\n')

par = 0
impar = 0
total_multiplicacion = 1
for i in lista_enteros:
    total_multiplicacion *=i
    if(EsParOImpar(i)):
       par+=1     
    else:
        impar+=1

print(f" >> Todos los números multiplicados dan como resultado {total_multiplicacion}.\n")

print(f" >> Hay {par} números pares y {impar} números impares en la lista.\n")

print(f" >> La lista final, sin números repetidos, es la siguiente: {sin_repetidos}")

