import os

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):    # Si la consola esta siendo ejecutada en Windows
        command = 'cls'             # El comando es alterado
    os.system(command)              # Se ejecuta 'cls' en vez de 'clear'