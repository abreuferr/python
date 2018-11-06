# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calculo de um polinomio binomial utilizando funcao
#               (n k) = n! / (k! * (n-k)!)

# funcao fatorial
#
def fatorial(valor):
    total = 1
    while (valor > 1):
        total = total * valor
        valor = valor - 1
    return total

# coleta de dados
#
valorN = int(input("Favor inserir o valor de N : "))
valorK = int(input("Favor inserir o valor de K : "))

# calcular o valor de (n-k)
#
valorNK = valorN - valorK

# chamada da funcao fatorial
#
n = fatorial(valorN)
k = fatorial(valorK)
nk = fatorial(valorNK)

# exibir os valores dos fatoriais
#
print("n! = ", n)
print("k! = ", k)
print("(n-k)! = ", nk)

# calcular o polinomio
#
polinomio = n / (k * (nk))

# exibir o resultado
#
print("o valor do polinomio eh : ", polinomio)