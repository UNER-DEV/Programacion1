# 3. Solicite al usuario su nombre 
# y luego solicite su apellido 
# y por último muestre el mensaje de salida “Hola nombre apellido”.

from modules.utils import *

clear()

nombre = input("Cual es su nombre? >> ")
apellido = input("Y su apellido? >> ")
print(f"\nHola {nombre} {apellido}\n")
