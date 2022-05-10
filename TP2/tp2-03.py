# 3. Que nos calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA 
# y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 21%

from modules.utils import *

clear()

def getMontoTotal(monto, IVA = 21):
    return float(round(monto * (IVA / 100 + 1), 2))

monto = float(input('Ingrese el monto sin IVA >> '))

msg = checkInputSiNo('\nDesea ingresar el IVA? >> ')

if(msg == 'si'):
    IVA = checkNumeroPositivo(float(input('\nIngrese el porcentaje de IVA a aplicar >> ')))
    print(f'\nEl monto final es de >> {getMontoTotal(monto,IVA)}\n')
elif(msg == 'no'):
    print('\n\t\tSe tomara en cuenta el 21% por defecto del IVA')
    print(f'\nEl monto final es de >> {getMontoTotal(monto)}\n')
