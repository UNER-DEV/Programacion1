#7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings con tareas  
# pendientes y la segunda almacenará strings con tareas terminadas. Permita al usuario:
    # a. Agregar nuevas tareas pendientes.
    # b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
    # de la lista de pendientes a la de terminadas.

# Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas.

from modules.utils import *

clear()

pendientes=[]
terminadas=[]

print("Buen día, vamos a organizar y añadir tareas a la agenda de hoy.")

def mostrarLista(list):
    if estaVacia(list,"Esta lista está vacía"):
        contador=1
        for i in list:
            print(f'{contador}- {i}')
            contador+=1

def finalizar_tarea():
    while True:
        print(f'\n\nTareas pendientes:')
        mostrarLista(pendientes)
        if not estaVacia(pendientes,""):
            break
        selector=normalizar(input("\n\nIngrese el número correspondiente a la tarea que finalizó >> "))
        terminadas.append(int(selector)-1)
        pendientes.pop(int(selector)-1)
        if estaVacia(pendientes,""):
            continuar= normalizar(input("\n¿Desea continuar finalizando tareas? Ingrese SI o NO  >> "))
            if continuar=="no":
                print(f'\nLista actual de tareas terminadas:')
                mostrarLista(terminadas)
                break
            if continuar!="si" and continuar !="no":
                print("\nUps, esa opción no existe. Por favor, ingrese una opción válida...\n\n")

def agregar_tarea():
        tarea= normalizar(input("\nIngrese una tarea pendiente por realizar >> "))
        pendientes.append(tarea)
        print(f'\n\nLista actual de tareas pendientes:')
        mostrarLista(pendientes)
        print(f'\nLista actual de tareas terminadas:')
        mostrarLista(terminadas)


while True:
    while True:
        selector=input("\n\n¿Qué desea hacer? ingrese:\n1-Para añadir una tarea.\n2-Para marcar como finalizada una tarea.\n3-Finalizar agenda.\n\nSu opción >> ")
        if(selector!="2" and selector!="1" and selector!="3"):
            print("Por favor,ingrese una opción válida")
        else:
            clear()
            break
    if selector=="2":
        finalizar_tarea()
    elif selector =="1":
        agregar_tarea()
    elif selector=="3":
        print(f'\n\nLista final de tareas pendientes:')
        mostrarLista(pendientes)
        print(f'\nLista final de tareas terminadas:')
        mostrarLista(terminadas)
        break


  


