# 10. Escriba un programa que indique si un texto es palíndromo, 
# es decir, se escribe igual al derecho que al revés. 
# Por ejemplo: rayar, kayak, somos.

from modules.utils import *

clear()

texto = str(input("Ingrese un texto: "))

if normalizar(texto).replace(" ","") == normalizar(texto[::-1]).replace(" ",""):
    print("\nEs palindromo\n")
else:
    print("\nNo es palindromo\n")