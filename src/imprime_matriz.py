# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : imprimir o conteudo de uma matriz

# funcao utilizada para imprimir o conteudo de uma matriz
def imprime_matriz(matriz):

    # obter as dimensoes da matriz
    linhas = len(matriz)
    colunas = len(matriz[0])

    # varredura da matriz
    for coordenada_i in range(linhas): # fazendo a varredura das linhas da matriz
        for coordenada_j in range(colunas): # fazendo a varredura das linhas da matriz
            # verifica se é a ultima celula da linha da matriz
            if(coordenada_j == colunas - 1):
                # imprimir o conteudo das linhas
                # %d - formato decimal
                # % - imprimir o conteudo
                print("%d" % matriz[coordenada_i][coordenada_j])
            # caso contrario
            else:
                # imprimir o conteudo das linhas
                # %d - formato decimanl
                # % - imprimir o conteudo
                print("%d" % matriz[coordenada_i][coordenada_j], end = " ")
    return

# main()
if __name__ == '__main__':  
    # matrizes para teste
    matriz_a = [[1], [2], [3]]
    matriz_b = [[1, 2, 3], [4, 5, 6]]

    # chamada da funcao imprime_matriz
    imprime_matriz(matriz_a)
    imprime_matriz(matriz_b)