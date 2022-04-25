# INTEGRANTES:
    # Camila Laureana Silva
    # Federico José Rodriguez
    # María Emilia Walter
    # Sebastian Ignacio Centurion

# 10. Escriba un programa que indique si un texto es palíndromo, 
# es decir, se escribe igual al derecho que al revés. 
# Por ejemplo: rayar, kayak, somos.

import console

console.clear()

texto = str(input("Ingrese un texto: "))

if texto.lower().replace(" ","") == texto[::-1].lower().replace(" ",""):
    print("\nEs palindromo\n")
else:
    print("\nNo es palindromo\n")