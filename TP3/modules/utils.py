import os
import sys

rutaUtils = os.path.abspath(__file__)           # Programacion1\TPX\modules\utils.py
rutaModules = os.path.dirname(rutaUtils)        # Programacion1\TPX\modules
ruta_tp = os.path.dirname(rutaModules)          # Programacion1\TPX
rutaProgramacion1 = os.path.dirname(ruta_tp)    # Programacion1
sys.path.append(rutaProgramacion1)              # Modifica la ruta actual

ruta_menu = os.path.join(ruta_tp,'menu.py')       # Programacion1\TPX\menu.py

from utils.console import *
from utils.list import *
from utils.numbers import *
from utils.strings import *