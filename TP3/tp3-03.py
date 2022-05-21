from modules.utils import *

# ----------------------------------------------------------------------------
# 3. Dada la siguiente lista de frutas ['banana', 'manzana', 'pera'],
# permitir al usuario ingresar 3 frutas mas para agregarlas al final de lista.
# Luego, mostrar por pantalla la lista completa y
# debajo la misma lista pero solo con las frutas que añadio el usuario
# ----------------------------------------------------------------------------

clear()

lst_frutas = ['banana','manzana','pera']

while True:
    print(f'\nLa lista de frutas actual es la siguiente: {lst_frutas}\n')
    if len(lst_frutas)==6:
        break
    fruta=normalizar(str(input('Por favor, ingrese una fruta distinta a la de la lista >> ')))
    clear()
    if fruta not in lst_frutas:
        lst_frutas.append(fruta)
    else:
        crearCartel('La fruta ya se encuentra en la lista. Ingrese otra...')

print(f'Lista completa >> {lst_frutas}\nFrutas que ingreso >> {lst_frutas[3:]}\n')

# ----------------------------------------------------------------------------

if(checkInputSiNo('Desea volver al MENU PRINCIPAL? >> ') == 'si'):
    exec(open(rutaMenu).read())
else:
    print(f'\n[Este programa ha finalizado]\n')
    exit()