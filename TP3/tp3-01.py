# 1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario)

from modules.utils import *

clear()

materias = ["Programación I","Introd. a la informática", "Programación II", "Arquitectura de computadoras", "Diseño gráfico"]

print("\nMaterias del primer cuatrimestre:\n")
for i in materias: 
    if i == materias[2]:
        print("\nMaterias del segundo cuatrimestre:\n")
    print(i)




