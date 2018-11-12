# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre matriz

# funcao para criar uma matriz e inserir valores
#
def cria_matriz(num_linhas, num_colunas):
    ''' (int, int) - matriz(lista de linhas)
    cria e retorna uma matriz com num_linhas linhas e 
    num_colunas colunas em que cada elemento é igual ao valor dado.
    '''

    # array vazio
    matriz = []

    # criar uma matriz com num_linhas de tamanho
    for i in range(num_linhas):
        
        # matriz vazia
        linha = []
        
        # criar uma matriz com num_colunas de tamanho
        for j in range(num_colunas):
            valor = int(input("digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        
        # adiciona linha a matriz
        matriz.append(linha)
    return matriz

# main
#
# colatar os dados
lin = int(input("digite o numero de linhas da matriz : "))
col = int(input("digite o numero de colunas da matriz : "))

# chamar a fucao cria_matriz e retorna e armazena o resultado
# em uma matriz
#
matriz = cria_matriz(lin, col)

# imprimir o resultado da matriz criada
#
print(matriz)