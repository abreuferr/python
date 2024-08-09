# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calcular a soma de duas matrizes

# importando a biblioteca.py
#
import biblioteca

def soma_matriz( matriz_a, matriz_b):
    numero_linhas = len(matriz_a)
    numero_colunas = len(matriz_a[0])

    # chamando a funcao para criar a uma matriz em branco
    # que vai conter o resultado da soma da matriz_a pela
    # matriz_b
    #
    matriz_c = biblioteca.cria_matriz(numero_linhas, numero_colunas, 0)

    for linha in range(numero_linhas): # percorre as linhas da matriz
        for coluna in range(numero_colunas): # percorre as colunas da matriz
            matriz_c[linha][coluna] = matriz_a[linha][coluna] + matriz_b[linha][coluna]
    
    return matriz_c

if __name__ == '__main__':  
    # matrizes para teste
    #
    matriz_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_b = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

    print(soma_matriz(matriz_a, matriz_b))