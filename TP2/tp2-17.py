# 17. Que imprima el siguiente patrón:
#   5 4 3 2 1
#   4 3 2 1
#   3 2 1
#   2 1
#   1

from modules.utils import *

clear()

for j in range(0, 5):
    for i in reversed(range(1, 6 - j)):
        print(i, end = ' ')
    print()
