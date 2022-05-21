from modules.utils import *

# ----------------------------------------------------------------------------------
# 1. Crear un programa que almacene en una lista las materias de esta u otra carrera 
# y que las muestre por pantalla. 
# (La lista debe ser predefinida, no debe ser ingresada por el usuario).
# ----------------------------------------------------------------------------------

clear()

lst_materias = ['Introduccion a la informatica','Programacion I','Diseno Grafico','Arquitectura de Computadoras','Programacion II', 'Sistemas Operativos', 'Introduccion al Desarrollo Web','Bases de datos','Redes de Datos','Programacion 3','Ingenieria de Software','Desarrollo de Aplicaciones Web','Desarrollo para Moviles','Multimedia y Juegos en Web']

print(f'{lst_materias}\n')

# ----------------------------------------------------------------------------------

if(checkInputSiNo('Desea volver al MENU PRINCIPAL? >> ') == 'si'):
    exec(open(ruta_menu).read())
else:
    print(f'\n[Este programa ha finalizado]\n')
    exit()
