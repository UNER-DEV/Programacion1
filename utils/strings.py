def crearCartel(str):
    espacios = ' ' * 20 
    centro = '|' + espacios + str + espacios + '|'
    borde = '-' * len(centro)
    print(f'{borde}\n{centro}\n{borde}')

def normalizar(str):
    reemplazo = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u")
    )
    for a, b in reemplazo:
        str = str.lower().replace(a, b)
    return str

def checkInputSiNo(value):
    while True:
        crearCartel('Ingrese por consola [SI] o [NO]')
        msg = normalizar(str(input(value)))
        if(msg == 'si' or msg == 'no'):
            break
    return msg

def checkInputSexo(value):
    while True:
        crearCartel('Ingrese por consola [F] por Femenino o [M] por Masculino')
        msg = normalizar(str(input(value)))
        if(msg == 'f' or msg == 'm'):
            break
    return msg