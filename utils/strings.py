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
        print('\n\t\tIngrese por consola [SI] o [NO]')
        msg = normalizar(str(input(value)))
        if(msg == 'si' or msg == 'no'):
            break
    return msg

def checkInputSexo(value):
    while True:
        print('\n\t\tIngrese por consola [F] por Femenino o [M] por Masculino')
        msg = normalizar(str(input(value)))
        if(msg == 'f' or msg == 'm'):
            break
    return msg