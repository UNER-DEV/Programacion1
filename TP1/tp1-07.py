# 7. Pida al usuario un número x de días 
# y luego mostrar por pantalla cuántas horas, minutos y segundos son esos números de días 

from modules.utils import *

clear()

cantDias = int(input("Ingrese una cantidad de dias >> "))

cantHoras = cantDias * 24
cantMinutos = cantHoras * 60
cantSegundos = cantMinutos * 60

print(f"\n{cantDias} dia/s tienen:")
print(f"\tHoras\t : {cantHoras}")
print(f"\tMinutos\t : {cantMinutos}")
print(f"\tSegundos : {cantSegundos}\n")
