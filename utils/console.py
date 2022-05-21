import os

rutaConsole = os.path.abspath(__file__)         # Programacion1\utils\console.py
rutaUtils = os.path.dirname(rutaConsole)        # Programacion1\utils
rutaProgramacion1 = os.path.dirname(rutaUtils)  # Programacion1
rutaTP = os.path.join(rutaProgramacion1, 'TP3') # Programacion1\TPX
rutaMenu = os.path.join(rutaTP,'menu.py')       # Programacion1\TPX\menu.py

def clear():
    command = 'clear'               # 'clear' es el comando ejecutable para los Sistemas Operativos MAC y Linux
    if os.name in ('nt', 'dos'):    # Si la consola esta siendo ejecutada en Windows
        command = 'cls'             # El comando es alterado
    os.system(command)              # Se ejecuta 'cls' en vez de 'clear'
