# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Esse programa tem como finalidade a de testar o Pytest

import pytest

# funcao fatorial
def fatorial(numero):
    # verifica o numero a ser calculado
    if numero < 0:
        return 0

    valor = fat = 1

    while (valor <= numero):
        fat = fat * valor
        valor -= 1
    return fat

# teste da funcao fatorial

@pytest.mark.parametrize("entrada, esperada", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    ])

def testa_fatorial0(entrada, esperada):
    assert fatorial(entrada) == esperada