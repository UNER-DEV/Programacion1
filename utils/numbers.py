import re

def esPrimo(num):
    value = True
    if num < 2:
        value = False
    else:
        for n in range(2,num):
            if (num%n == 0):
                value = False
    return value

def checkNumeroPositivo(num):
    while True:
        if(float(num) >= 0):
            break
        num = float(input('\nEl numero ingresado debe ser mayor o igual a 0, intente nuevamente >> '))
    return num

def potenciar(base, exp):
    return int(base ** exp)

def getAreaTriangulo(base, altura):
    return float((base * altura)/2)

def EsParOImpar(num):
    value=True
    if(num%2 != 0):
        value=False
    return value

def checkNumero(num):
    check = re.compile(r'^\-?[1-9][0-9]*$')
    value = re.match(check,num)
    if value:
        return num
    else:
        print("Por favor, ingrese un número y no otro caracter")

