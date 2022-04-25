# INTEGRANTES:
    # Camila Laureana Silva
    # Federico José Rodriguez
    # María Emilia Walter
    # Sebastian Ignacio Centurion

# 13. Programe una aplicación de consola que 
# solicite al usuario su nombre, después su apellido y a continuación su año de nacimiento. 
# Con esos datos deberá generar una sugerencia de usuario y contraseña. 
# Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento: 1985 
# -> Usuario: mfrancisconi, Contraseña: mf.1985.

import console

console.clear()

# FUNCION
def generarDatos(param1,param2,param3):
    print(f"\nUsuario: {(param1[0] + param2).lower()}")
    print(f"Contrasenia: {(param1[0] + param2[0] + '.' + param3).lower()}\n")

nombre = str(input("Ingrese nombre >> "))
apellido = str(input("Ingrese apellido >> "))
anio = str(input("Ingrese su anio de nacimiento >> "))

generarDatos(nombre,apellido,anio)
