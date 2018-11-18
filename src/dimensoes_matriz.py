# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : funcao que define o tamanho de uma matriz

# funcao para definir o tamanho da matriz
def dimensoes(matriz):
    numero_linha = len(matriz)
    numero_coluna = len(matriz[0])

    # retorna os resultados
    return numero_linha, numero_coluna

# main()
if __name__ == '__main__':
    # dados a serem verificados
    matriz = [[1, 2, 3], [4, 5, 6]]

    # chama a matriz para calcular o numero
    # de linha e coluna
    resultado = dimensoes(matriz)

    # a variavel resultado retorna com dois valores
    # que sao armazenados nas variaveis valor_i e
    # valor_j
    valor_i, valor_j = resultado

    # exibe o resultado das dimensoes da matriz
    print("{:d}X{:d}".format(valor_i, valor_j))