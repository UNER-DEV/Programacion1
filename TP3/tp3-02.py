from modules.utils import *

# --------------------------------------------------
# 2. Pedir al usuario que ingrese 5 números 
# para luego almacenarlos en una lista y ordenarlos.
# Imprimir por pantalla el resultado.
# --------------------------------------------------

clear()

lst_numeros = []

for i in range(0,5):
    while True:
        crearCartel('Por favor, ingrese un numero y no otro caracter')
        elemento = input(f'Ingrese el #{i+1} numero >> ')
        clear()
        if elemento.isnumeric():
            lst_numeros.append(int(elemento))
            break

print(f'\nLa lista ordenada es la siguiente: {sorted(lst_numeros)}\n')

# --------------------------------------------------

if(checkInputSiNo('Desea volver al MENU PRINCIPAL? >> ') == 'si'):
    exec(open(rutaMenu).read())
else:
    print(f'\n[Este programa ha finalizado]\n')
    exit()