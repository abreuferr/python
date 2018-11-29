# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calcular a soma de duas matrizes

# importando biblioteca
import biblioteca

# funcao utilizada para calcular a soma das matrizes
def soma_matrizes(matriz_a, matriz_b):
    numero_linhas = len(matriz_a) # numero de linhas da matriz_a
    numero_colunas = len(matriz_a[0]) # numero de colunas da matriz_a

    matriz_c = biblioteca.cria_matriz(numero_linhas, numero_colunas, 0) # chama funcao cria_matriz

    for linha in range(numero_linhas): # percorre as linhas da matriz
        for coluna in range(numero_colunas): # percorre as colunas da matriz
            matriz_c[linha][coluna] = matriz_a[linha][coluna] + matriz_b[linha][coluna]
    return matriz_c

# main()
if __name__ == '__main__':  
    # matrizes para teste
    matriz_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_b = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

    print(soma_matrizes(matriz_a, matriz_b))