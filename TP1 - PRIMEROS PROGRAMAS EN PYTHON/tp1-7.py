# 7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
# segundos son esos números de días 

import console

console.clear()

print("Ingrese una cantidad de días:")
cantDias = int(input())

cantHoras = cantDias * 24
cantMinutos = cantHoras * 60
cantSegundos = cantMinutos * 60

print(f"\n{cantDias} dias tienen:")
print(f"\tHoras\t : {cantHoras}")
print(f"\tMinutos\t : {cantMinutos}")
print(f"\tSegundos : {cantSegundos}\n")
