# 10. Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
# derecho que al revés. Por ejemplo: rayar, kayak, somos.

import console

console.clear()

texto = str(input("Ingrese un texto: "))

if texto == texto[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")