def remove_repetidos(lista):
    lista = sorted(lista)
    lista_nova = []
    for i in range(len(lista)):
        if lista[i] != lista[i-1]:
            lista_nova.append(lista[i])
    
    return lista_nova
    
