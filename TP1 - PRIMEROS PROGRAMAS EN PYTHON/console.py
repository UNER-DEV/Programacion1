# INTEGRANTES:
    # Camila Laureana Silva
    # Federico José Rodriguez
    # María Emilia Walter
    # Sebastian Ignacio Centurion

import os                           # Modulo que nos provee funcionalidades del Sistema Operativo

def clear():
    command = 'clear'               # 'clear' es el comando ejecutable para los Sistemas Operativos MAC y Linux
    if os.name in ('nt', 'dos'):    # Si la consola esta siendo ejecutada en Windows
        command = 'cls'             # El comando es alterado
    os.system(command)              # Se ejecuta 'cls' en vez de 'clear'