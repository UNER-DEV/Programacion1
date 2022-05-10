# 13. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje 
# si es lunes, otro mensaje diferente 
# si es viernes, otro mensaje diferente 
# si es sábado o domingo. 
# Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

from modules.utils import *

clear()

str = normalizar(str(input('Ingrese un dia de la semana >> ')))

if(str == 'lunes'):
    print('\nQue amargos los Lunes!!!\n')
elif(str == 'viernes'):
    print('\nQue lindos los Viernes!!!\n')
elif(str == 'sabado' or str == 'domingo'):
    print('\nLlego el finde!!! Hoy me la doy en la pera, y veo el Super Clasico!!!\n')
else:
    print('\nEs un dia cualquiera\n')
