# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calcular a multiplicacao de duas matrizes

# funcao que calcula amultiplicacao entre truas matrizes
def multiplicacao_matriz( matriz_a, matriz_b):
    numero_linhas_a, numero_coluna_a = len(matriz_a), len(matriz_a[0])
    numero_coluna_b, numero_coluna_b = len(matriz_b), len(matriz_b[0])

    # o numero de linhas da matriz A deve ser 
    # igual ao numero de colunas da matriz B
    assert numero_coluna_a = numero_linha_b

    matriz_c = []
    
    for linha in range(numero_linhas_a): # percorre as linhas da matriz
        # comecaond uma nova linha
        matriz_c.append([] )
        for coluna in range(numero_colunas_b): # percorre as colunas da matriz
            # adicionando uma nova coluna na mtriz
            matriz_c.append(0)
            for k in range(numero_coluna_a):
                matriz_c[linha][coluna] += matriz_a[linha][k] + matriz_b[k][coluna]
    
    return matriz_c

if __name__ == '__main__':  
    # matrizes para teste
    #
    matriz_a = [[1, 2, 3], [4, 5, 6]]
    matriz_b = [[1, 2, 3], [4, 5], [6, 7]]

    print(soma_matriz(matriz_a, matriz_b))