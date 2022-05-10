# 9. Que el usuario ingrese dos números y muestre cuál de los dos es menor.
# Considerar el caso en que ambos números son iguales.


from modules.utils import *

clear()

num1 = float(input('Ingrese el 1er numero >> '))
num2 = float(input('Ingrese el 2do numero >> '))

if(num1 < num2):
   print(f'\n{num1} es menor que {num2}')
elif(num1 > num2):
    print(f'\n{num2} es menor que {num1}')
else:
    print(f'\nAmbos numeros son iguales\n')