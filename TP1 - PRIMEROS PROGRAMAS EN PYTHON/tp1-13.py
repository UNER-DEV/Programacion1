# 13. Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
# a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
# usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
# 1985 -> Usuario: mfrancisconi, Contraseña: mf.1985.

import console

console.clear()

# FUNCIONES
def generarUsuario(param1, param2):
    return (param1[0] + param2).lower()

def generarContrasenia(param1,param2,param3):
    return (param1[0] + param2[0] + "." + param3).lower()

nombre = str(input("Ingrese nombre >> "))
apellido = str(input("Ingrese apellido >> "))
anio = str(input("Ingrese su año de nacimiento >> "))

print(generarUsuario(nombre,apellido))
print(generarContrasenia(nombre,apellido,anio))
