from modules.utils import *

clear()

for j in range(0, 5):
    for i in reversed(range(1, 6 - j)):
        print(i, end = ' ')
    print()
