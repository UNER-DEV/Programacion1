# 11. Programe una aplicación de consola que muestre los primeros 5 caracteres de una cadena
# de texto ingresada por el usuario.

import console

console.clear()

msg = str(input("Ingrese un mensaje: "))

print(msg[0:5])