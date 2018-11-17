# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : biblioteca de funcoes

# funcao para calcular o valor de fibonacci
#
def fib1(numero):
    valor_a, valor_b = 0, 1
    while valor_b < numero:
        print(valor_b, end=' ')
        valor_a, valor_b =  valor_b, valor_a + valor_b
    print()

def fib2(numero):
    resultado = []
    valor_a, valor_b = 0, 1
    while valor_b < numero:
        resultado.append(valor_b)
        valor_a, valor_b = valor_b, valor_a + valor_b
    return resultado

# funcao para criar uma matriz e inserir valores
#
def cria_matriz(num_linhas, num_colunas, valor):
    ''' (int, int, int) - matriz(lista de linhas)
    cria e retorna uma matriz com num_linhas linhas e 
    num_colunas colunas em que cada elemento é igual ao valor dado.
    '''
    # matriz vazia
    matriz = []

    # criar uma matriz com num_linhas de tamanho
    for coordenada_i in range(num_linhas):
        
        # matriz vazia
        linha = []
        
        # criar uma matriz com num_colunas de tamanho
        for coordenada_j in range(num_colunas):
            linha.append(valor)
        
        # adiciona linha a matriz
        matriz.append(linha)
    return matriz