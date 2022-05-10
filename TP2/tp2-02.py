# 2. Que reciba un número entero positivo 
# y una potencia a elevar 
# y que nos devuelva el resultado.

from modules.utils import *

clear()

base = int(checkNumeroPositivo(int(input('Ingrese la base >> '))))
exp = int(checkNumeroPositivo(int(input('\nIngrese el exponente >> '))))

print(f'\nLa potencia es >> {base} ^ {exp} = {potenciar(base, exp)}\n')
