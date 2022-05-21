import os
from modules.utils import *


enunciados = '1234567'

while True:
    clear()
    crearCartel('MENU PRINCIPAL')
    e = normalizar(input('Recuerde que este TP contiene 7 enunciados\nPuede ingresar el numero del enunciado\nO escribir [SALIR] para finalizar el programa.\nQue desea ejecutar? >> '))
    if(e in enunciados and len(e) == 1):
        program = 'tp3-0' + e + '.py'
        rutaEnun = os.path.join(ruta_tp, program)
        exec(open(rutaEnun).read())
        break
    elif e == 'salir':
        print(f'\n[Este programa ha finalizado]\n')
        exit()
