def quitarRepetidos(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result

def ordenarLista(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista

def estaVacia(miLista,mensaje):
    if miLista: 
        return miLista
    print(mensaje, end = ' ')
    return False  