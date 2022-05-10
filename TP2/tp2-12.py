from modules.utils import *

clear()

def countVocales(str):
    vocales = 'aeiou'
    contador = 0
    for i in normalizar(str):
        if i in vocales:
            contador += 1
    return contador

str = input("Escriba un mensaje >> ")

print(f'\n{str} tiene {countVocales(str)} vocales\n')
