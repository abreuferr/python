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

lista = [7,3,33,12,3,3,3,7,12,100]

lista = remove_repetidos(lista)
print (lista)