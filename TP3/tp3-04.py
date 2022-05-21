# 4.Dada la siguiente lista: países = ['Argentina,'Brasil', 'Bolivia','Paraguay','Venezuela'], 
# realizar lo siguiente:
    # a. Imprimir la cantidad de elementos que tiene la lista
    # b. Imprimir el primer y último elemento.
    # c. Imprimir el resto.
    # d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
    # la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
    # e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
    # la lista. Quitar el elemento correspondiente de esa posición.
    # f. Imprimir la lista en orden inverso.
    # g. Vaciar la lista



from modules.utils import *

clear()

paises = ['Argentina','Brasil', 'Bolivia','Paraguay','Venezuela']
print(f"La lista de paises es la siguiente {paises} y tiene {len(paises)} elementos.\n")
print(f"El primer elemento de la lista es {paises[0]} y el último {paises[-1]}.\n")

print(f"Esta lista, además tiene estos otros países >> {paises[1:-1]}.\n")

while True:
    nuevo_pais=(normalizar(input("Ahora bien, observando la lista completa de paises...\nEscriba el nombre de algún país que existe en ella >> "))).capitalize()
    if(nuevo_pais in paises):
        print(f"\nEl país ingresado está en la posición {paises.index(nuevo_pais)}.\n")
        break
    print(f"\nUps, el país ingresado no se encuentra en la lista. Probemos nuevamente...\n")

total=int(len(paises))


while True:
    num=(int(checkNumeroPositivo(input("Ingresá la cantidad total o menor de paises que ves en la lista >> ")))-1)
    if(num <= total and num !=-1):
        print(f"\n¡Muy bien! Te cuento que en la posición {num} se encuentra el país {paises[num]}.")
        nuevaLista=paises.pop(num)
        print(f"\nSi lo eliminamos, nuestra lista queda de esta manera >> {paises}\n")
        break
    else:
        print(f"\nUps, recordá que debes ingresar un número mayor a 0.\n")


paises.reverse() # Otra opción => paises[::-1]

print(f"Y sí la invertimos, nos quedaría {paises}")

paises.clear() 
