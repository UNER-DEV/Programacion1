# 3.Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3 frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y debajo la misma lista pero sólo con las frutas que añadió el usuario.

from modules.utils import *

clear()

lista_frutas = ['banana', 'manzana', 'pera']
nueva_lista = []


while True:
    print(f"\nLa lista de frutas actual es la siguiente: {lista_frutas+nueva_lista}\n")
    if len(nueva_lista)==3:
        break
    fruta=normalizar(input('Por favor, ingrese una fruta distinta a la de la lista >> '))
    if fruta not in lista_frutas and fruta not in nueva_lista:
        nueva_lista.append(fruta)
    else:
        print(f"\nLa fruta ya se encuentra en la lista. Ingrese otra... \n")


clear()    
print(f"\nLa lista completa de frutas es la siguiente: {lista_frutas+nueva_lista}\n")
print(f"\nLas frutas ingresadas por el usuario son: {nueva_lista}\n")

