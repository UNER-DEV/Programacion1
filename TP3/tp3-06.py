from modules.utils import *

# ----------------------------------------------------------------------------------------------------------------
# 6.Programe una aplicacion de consola Python que brinde al usuario la posibilidad de a partir de una lista vacia:
    # a. Agregar un elemento al final.
    # b. Agregar un elemento al principio.
    # c. Quitar un elemento al final.
    # d. Quitar un elemento al principio
# ----------------------------------------------------------------------------------------------------------------

clear()

miLista=[]

def opciones(op):
    if(op == '1' or op == '2'):
        while True:
            elemento = input('\nIngrese un numero >> ')
            if elemento.isnumeric():
                return elemento
    elif op =='3':
        print(f'Su lista es la siguiente: {miLista}\nY se ha quitado el elemento {miLista.pop(-1)}.\n')
    elif op=='4':
        print(f'Su lista es la siguiente: {miLista}\nY se ha quitado el elemento {miLista.pop(0)}.\n')
            
def loopIngreso():
    clear()
    while True:
        print(f'Su lista actual es: {miLista}')
        selector=input('Ingrese:\n1-Para agregar un elemento al final.\n2-Para agregar un elemento al principio.\n3-Para quitar un elemento al final de la lista.\n4-Para quitar un elemento del principio.\n\nSu opcion >> ')
        if selector == '1':
            miLista.insert(len(miLista),int(opciones(selector)))
            break
        elif selector == '2':
            miLista.insert(0,int(opciones(selector)))
            break
        elif(selector=='3' or selector=='4'):
            if estaVacia(miLista, 'La lista esta vacia.'):
                opciones(selector)
                break
            clear()
        else:
            print('\nUps, esa opcion no existe. Por favor, ingrese una opcion valida...')

print('Buen dia! vamos a agregar elementos a una lista.\n')
while True:
    continuar=normalizar(input('\nDesea agregar o quitar un numero? Ingrese SI o NO >> '))
    if continuar=='si':
        loopIngreso()
    elif continuar== 'no':
        print(f'\n\nGracias por su colaboracion.')
        if(estaVacia(miLista,"Su lista final esta vacia\n\n")): 
            print(f'Su lista final es: {miLista}\n')
        break

# ----------------------------------------------------------------------------------------------------------------

if(checkInputSiNo('Desea volver al MENU PRINCIPAL? >> ') == 'si'):
    exec(open(rutaMenu).read())
else:
    print(f'\n[Este programa ha finalizado]\n')
    exit()
