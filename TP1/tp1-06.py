# 6. Programe una aplicación de consola que pregunte el precio total de la cuenta, 
# luego pregunte cuántos comensales hay. 
# A continuación deberá dividir la cuenta total por el número de comensales 
# y mostrar cuánto debe pagar cada persona.

from modules.utils import *

clear()

precio = float(input("Indique el precio total de la cuenta >> $ "))
numComensales = int(input("Indique la cantidad de comensales >> "))

print(f"\n${precio} entre {numComensales} comensales, cada persona debe pagar: ${round(precio / numComensales, 2)}\n")
