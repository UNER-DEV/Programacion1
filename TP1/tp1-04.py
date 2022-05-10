# 4. Pida al usuario que ingrese 2 números 
# para luego sumarlos 
# y mostrar en pantalla: “La respuesta es XX”.

from modules.utils import *

clear()
    
numero1 = int(input("Ingrese el 1er numero  >>  "))
numero2 = int(input("Ingrese el 2do numero  >>  "))
print(f"\nLA RESPUESTA ES >> {numero1} + {numero2} = {numero1 + numero2}\n")
