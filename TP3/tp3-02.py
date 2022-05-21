# 2.Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
# Imprimir por pantalla el resultado.

from modules.utils import *

clear()

def lista_ordenada(numeros):
    list1 = list(map(int, numeros.split()))
    return sorted(list1)
    


while True:
    num=input('Ingrese 5 números aleatorios separados por un espacio >> ')
    if len(num.split())==5:
        print(f"\nLos números ingresados en orden ascendente son {lista_ordenada(num)}")
        break
    clear()
    print(f"No introdujo la cantidad correspondiente de números. Intente nuevamente...\n")
        
    

