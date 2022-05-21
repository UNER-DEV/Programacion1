from modules.utils import *

# ----------------------------------------------------------------------------------------------
# 4.Dada la siguiente lista: paises = ['Argentina,'Brasil','Bolivia','Paraguay','Venezuela'], 
# realizar lo siguiente:
    # a. Imprimir la cantidad de elementos que tiene la lista
    # b. Imprimir el primer y ultimo elemento.
    # c. Imprimir el resto.
    # d. Permitir que el usuario ingrese un pais e imprimir el indice si el pais se encuentra en
    # la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
    # e. Permitir al usuario ingresar un numero igual o menor a la cantidad de elementos de
    # la lista. Quitar el elemento correspondiente de esa posicion.
    # f. Imprimir la lista en orden inverso.
    # g. Vaciar la lista
# ----------------------------------------------------------------------------------------------

clear()

lst_paises = ['Argentina','Brasil','Bolivia','Paraguay','Venezuela']
mostrar_paises = '\nAhora bien, observando la lista completa de paises: ' + str(lst_paises) + '\n'
print(f'La lista de paises es la siguiente {lst_paises} y tiene {len(lst_paises)} elementos.')
print(f'El primer elemento de la lista es [{lst_paises[0]}] y el ultimo es [{lst_paises[-1]}].')
print(f'Ademas, contiene estos otros paises: {lst_paises[1:-1]}')

while True:
    pais = normalizar(input(f'\nAhora bien, observando la lista completa de paises: {lst_paises}\nEscriba el nombre de algun pais que existe en ella >> ')).capitalize()
    if(pais in lst_paises):
        print(f'\n\t\t- El pais ingresado esta en la posicion {lst_paises.index(pais) + 1}.\n')
        break
    print('\nUps, el pais ingresado no se encuentra en la lista. Probemos nuevamente...')

while True:
    num = int(input('Ingrese un numero entre 1 y 5 >> '))
    if(num > 0 and num <= len(lst_paises)):
        del lst_paises[num-1]
        break

print(f'\n\t\t- Acaba de eliminar el elemento numero {num}')
print(f'\n\t\t- La lista ahora se ve de esta manera >> {lst_paises}')

lst_paises.reverse()

print(f'\nEsta es la misma lista al reves >> {lst_paises}')

lst_paises.clear()

print(f'\nEsta lista ahora esta vacia >> {lst_paises}\n')

# ----------------------------------------------------------------------------------------------

if(checkInputSiNo('Desea volver al MENU PRINCIPAL? >> ') == 'si'):
    exec(open(rutaMenu).read())
else:
    print(f'\n[Este programa ha finalizado]\n')
    exit()
