# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calcular a multiplicacao de duas matrizes

# funcao utilizada para definir o tamanho da matriz
def dimensao(minha_matriz):
    numero_linha = len(minha_matriz)
    numero_coluna = len(minha_matriz[0])

    # retorna os resultados
    return numero_linha, numero_coluna

# funcao que calcula a multiplicacao entre duas matrizes
def multiplicacao_matriz(matriz_a, matriz_b):
    numero_linhas_a, numero_colunas_a = len(matriz_a), len(matriz_a[0])
    numero_linhas_b, numero_colunas_b = len(matriz_b), len(matriz_b[0])

    # o numero de linhas da matriz A deve ser 
    # igual ao numero de colunas da matriz B
    assert numero_colunas_a == numero_linhas_b

    matriz_c = []
    
    for linha in range(numero_linhas_a): # percorre as linhas da matriz
        # comecaond uma nova linha
        matriz_c.append([])
        for coluna in range(numero_colunas_b): # percorre as colunas da matriz
            # adicionando uma nova coluna na linha
            matriz_c[linha].append(0)
            for contador in range(numero_colunas_a):
                matriz_c[linha][coluna] += matriz_a[linha][contador] * matriz_b[contador][coluna]
    return matriz_c

# main()
if __name__ == '__main__':  
    # matrizes para teste
    matriz_a = [[1, 2, 3], [4, 5, 6]]
    matriz_b = [[1, 2], [3, 4], [5, 6]]

    # resultado da multiplicacao das matrizes_a X matriz_b
    print(multiplicacao_matriz(matriz_a, matriz_b))