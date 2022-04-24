# 5. Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
# luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
# forma: “La respuesta es XX”.

import console

console.clear()

def operacion(num1,num2,num3):
    return (num1 + num2) * num3

numero1 = int(input("Ingrese el primer número    >> "))
numero2 = int(input("\nIngrese el segundo número >> "))
numero3 = int(input("\nIngrese el tercer número  >> "))

print(f"\nOperación formada >> ({numero1} + {numero2}) * {numero3} = {operacion(numero1,numero2,numero3)}\n")
