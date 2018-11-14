# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : biblioteca

# modulo para calcular o valor de fibonacci
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