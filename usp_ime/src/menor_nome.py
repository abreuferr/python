# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : o programa deve encontrar o menor nome dentro de uma string

def normalizacao(nomes):
    # remover os espacos em branco dos nomes
    array_auxiliar_1 = []
    for caractere in nomes:
        auxiliar = caractere.replace(' ','')
        array_auxiliar_1.append(auxiliar)

    # substituir caracteres maiusculos por minusculos
    # dos nomes
    array_auxiliar_2 = []
    for contador in array_auxiliar_1:
        nome_minusculo = contador.lower()
        array_auxiliar_2.append(nome_minusculo)

    # substituir a primeira letra do nome por maiuscula
    array_auxiliar_3 = []
    for contador in array_auxiliar_2:
        nome_maiuscula = contador.capitalize()
        array_auxiliar_3.append(nome_maiuscula)

    return array_auxiliar_3

# funcao utilizada para encontrar o menor nome
def menor_nome(nomes):
    tamanho_menor_nome = 1000
    tamanho_nome = 0 

    # chamando funcao para normalizar os nomes
    nomes_normalizados = normalizacao(nomes)

    for nome in nomes_normalizados: # varrer o array com os nomes
        tamanho_nome = len(nome) # extrair no tamanho de cada nome

        if tamanho_menor_nome > tamanho_nome:
            menor_nome = nome
            tamanho_menor_nome = tamanho_nome

    return menor_nome

# deve devolver 'Ito'
nomes = ['maria', 'josé', 'PAULO', 'Catarina']
menor_nome(nomes)

# deve devolver 'José'
nomes = ['maria', ' josé ', '   PAULO', 'Catarina   ']
menor_nome(nomes)

# deve devolver José
nomes = ['LU   ', ' josé ', 'PAULO', 'Catarina']
menor_nome(nomes)

nomes = ['zé', ' lu', 'fê']
menor_nome(nomes)