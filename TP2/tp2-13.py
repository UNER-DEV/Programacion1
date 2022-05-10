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
