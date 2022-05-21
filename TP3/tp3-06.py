# 6.Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir de una lista vacía:
    # a. Agregar un elemento al final.
    # b. Agregar un elemento al principio.
    # c. Quitar un elemento al final.
    # d. Quitar un elemento al principio

from modules.utils import *

clear()

miLista=[]


def opciones(op):
    if(op == "1" or op == "2"):
        elemento=checkNumero(input("\nIngrese un número >> "))
        return elemento
    elif op =="3":
        print(f"Su lista es la siguiente: {miLista}")
        removed_element = miLista.pop(-1)
        print(f"y se ha quitado el elemento {removed_element}. Su lista actualizada es {miLista}\n")
    elif op=="4":
        print(f"Su lista es la siguiente: {miLista}")
        removed_element = miLista.pop(0)
        print(f"y se ha quitado el elemento {removed_element}. Su lista actualizada {miLista} \n")
            


def loopIngreso():
    while True:
        selector=input("\n\nIngrese:\n1-Para añadir un elemento al final.\n2-Para añadir un elemento al principio.\n3-Para quitar un elemento al final de la lista.\n4-Para quitar un elemento del principio.\n\nSu opción >> ")
        if selector == "1":
            miLista.insert(len(miLista),int(opciones(selector)))
            break
        elif selector == "2":
            miLista.insert(0,int(opciones(selector)))
            break
        elif(selector=="3" or selector=="4"):
            if estaVacia(miLista, "La lista está vacía."):
                opciones(selector)
                break
            clear()
        else:
            print("\nUps, esa opción no existe. Por favor, ingrese una opción válida...\n\n")


print("¡Buen día! vamos a añadir elementos a una lista.\n")
while True:
    continuar=normalizar(input("\n¿Desea añadir o quitar un número? Ingrese SI o NO >> "))
    if continuar=="si":
        loopIngreso()
    elif continuar== "no":
        print(f"\n\nGracias por su colaboración. Su lista final {estaVacia(miLista,'está vacía')}")
        break



 
