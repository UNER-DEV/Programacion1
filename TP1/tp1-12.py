# 12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa 
# e imprimir en pantalla el día, mes y año. 
# Ej: Usuario ingresa: 17/05/1985
# Programa imprime: Día: 17, Mes: 05 y Año: 1985

import re
from modules.utils import *

clear()

while True:
    formato = "^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$"
    fecha = str(input("Ingrese una fecha en formato Dia/Mes/Anio >> "))
    if(re.match(formato, fecha)):
        break

print(f"\nDia: {fecha[0:2]}, Mes: {fecha[3:5]}, Anio: {fecha[6:10]}\n")
