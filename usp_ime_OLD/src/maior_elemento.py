def remove_repetidos(lista):
    lista_final = []
    for contador in lista:
        if contador not in lista_final:
            lista_final.append(contador)
    lista_final.sort()
    return lista_final

def soma_elementos(lista):
    # soma de todos os elementros do array "lista"
    total = sum(lista)
    return total

def maior_elemento(lista):
    lista.sort()
    ultima_celula = lista[len(lista)-1]
    return ultima_celula

lista = [1,7,4,0]

lista = remove_repetidos(lista)
maior_numero = maior_elemento(lista)