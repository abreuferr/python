# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Esse programa tem como finalidade a de calcular o valor
#               do fatorial de um determinado numero e realizar teste
#               automatizados.

# funcao fatorial
#
def fatorial(valor):
    valorFatorial = 1
    while (valor > 1):
        valorFatorial = valorFatorial * valor
        valor = valor - 1
    return valorFatorial

# funcao binomial
#
def binomial(valorN, valorK):
    return fatorial(valorN) / ( fatorial(valorK) * fatorial(valorN - valorK))

#  teste da funcao fatorial
#
if fatorial(1) == 1:
    print("funciona para 1")
else:
    print("Nao funciona para 1")
if fatorial(2) == 2:
    print("funciona para 2")
else:
    print("Nao funciona para 2")
if fatorial(5) == 120:
    print("funciona para 5")
else:
    print("Nao funciona para 5")

#  teste da funcao binomial
#
if binomial(5, 3) == 10:
    print("funciona para 5 e 3")
else:
    print("Nao funciona para 5 e 3")