# AUTORES : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# TITULO  : Ordem lexicografica
''' 
Escreva a funcao primeiro_lex(lista) que recebe uma lista
de strings como parametro e devolve o primeiro string na
ordem lexicografica. Neste exercicio, considere letras
maiusculas e minusculas.
'''

def primeiro_lex(lista):
    valor_controle = 10000
    for contador in range(len(lista)): 
        nome = lista[contador] # extrair o conteudo do array
        primeiro_caractere = nome[0] # primeiro caracter da palavra
        valor_ascii = ord(primeiro_caractere) # codigo ascii do caractere

        if valor_controle > valor_ascii:
            valor_controle = valor_ascii
            menor_nome = nome

    return menor_nome # retorna com o menor nome lexicografico

# main()
primeiro_lex(['maria', 'jose', 'Catarina', 'PAULO']) # deve devolver 'Catarina'
primeiro_lex(['ze', 'lu', 'fe']) # deve devolver 'fe'