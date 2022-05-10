import os
import sys

rutaUtils = os.path.abspath(__file__)           # Programacion1\TPX\modules\utils.py
rutaModules = os.path.dirname(rutaUtils)        # Programacion1\TPX\modules
rutaTP = os.path.dirname(rutaModules)           # Programacion1\TPX
rutaProgramacion1 = os.path.dirname(rutaTP)     # Programacion1
sys.path.append(rutaProgramacion1)              # Modifica la ruta actual

from utils.console import *
from utils.strings import *