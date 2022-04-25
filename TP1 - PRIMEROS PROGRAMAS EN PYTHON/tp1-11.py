# INTEGRANTES:
    # Camila Laureana Silva
    # Federico José Rodriguez
    # María Emilia Walter
    # Sebastian Ignacio Centurion

# 11. Programe una aplicación de consola que muestre los primeros 5 caracteres de una cadena de texto ingresada por el usuario.

import console

console.clear()

msg = str(input("Ingrese un mensaje: "))

print(f"\nPrimeros 5 caracteres: [{msg[0:5]}]\n")