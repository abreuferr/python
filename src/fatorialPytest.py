# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Esse programa tem como finalidade a de testar o Pytest

# funcao fatorial
#
def fatorial(valor):
    # verifica o numero a ser calculado
    #
    if valor < 0
        return 0

    valorFatorial = 1
    while (valor > 1):
        valorFatorial = valorFatorial * valor
        valor = valor - 1
    return valorFatorial

# teste da funcao fatorial
#
def teste_fatorial0():
    assert fatorial(0) == 1

def teste_fatorial1():
    assert fatorial(1) == 1

def teste_fatorialNegativo():
    assert fatorial(-10) == 0

def teste_fatorial4():
    assert fatorial(4) == 24

def teste_fatorial5():
    assert fatorial(5) == 120
