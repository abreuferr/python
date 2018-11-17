# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : funcao que define o tamanho de uma matriz

# funcao para definir o tamanho da matriz
def dimensoes(minha_matriz):
    numero_linha = len(minha_matriz)
    numero_coluna = len(minha_matriz[0])

    # retorna os resultados
    return numero_linha, numero_coluna

# main()
if __name__ == '__main__':
    # dados a serem verificados
    minha_matriz = [[1, 2, 3], [4, 5, 6]]

    # chama a matriz para calcular o numero
    # de linha e coluna
    resultado = dimensoes(minha_matriz)

    # exibe o resultado das dimensoes da matriz
    print(resultado)