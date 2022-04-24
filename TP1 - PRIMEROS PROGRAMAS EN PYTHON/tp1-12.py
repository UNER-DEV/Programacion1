# 12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
# día, mes y año. Ej:
# Usuario ingresa: 17/05/1985
# Programa imprime: Día: 17, Mes: 05 y Año: 1985

import console

console.clear()

fecha = str(input("fecha: "))

print(f"dia: {fecha[0:2]}, mes: {fecha[3:5]}, año: {fecha[6:10]}")
