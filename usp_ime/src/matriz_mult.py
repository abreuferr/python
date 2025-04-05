# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : verificar se é possivel multiplicar duas matrizes

# funcao utilizada para definir o tamanho da matriz
def dimensao(minha_matriz):
    numero_linha = len(minha_matriz)
    numero_coluna = len(minha_matriz[0])

    # retorna os resultados
    return numero_linha, numero_coluna

# main()
if __name__ == '__main__':  
    # matrizes para teste
    matriz_a = [[1, 2, 3], [4, 5, 6]]
    matriz_b = [[2, 3, 4], [5, 6, 7]]
    matriz_a = [[1], [2], [3]]
    matriz_b = [[1, 2, 3]]

    # o número de colunas da matriz_a deve ser igual ao número de linhas da matriz_b
    numero_linha_matriz_a, numero_coluna_matriz_a = dimensao(matriz_a)
    numero_linha_matriz_b, numero_coluna_matriz_b = dimensao(matriz_b)
    
    # verifica se é possivel multiplicar as matrizes
    if numero_coluna_matriz_a == numero_linha_matriz_b:
        print("É possivel multiplicar a matriz ", matriz_a, "pela matriz ", matriz_b)
    else:
        print("Não é possivel multiplicar a matriz ", matriz_a, "pela matriz ", matriz_b)