# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calculo de um polinomio binomial utilizando funcao
#               (n k) = n! / (k! * (n-k)!)

# funcao fatorial
#
def fatorial(valor):
    valorFatorial = 1
    while (valor > 1):
        valorFatorial = valorFatorial * valor
        valor = valor - 1
    return valorFatorial

# coleta de dados
#
valorN = int(input("Favor inserir o valor de N : "))
valorK = int(input("Favor inserir o valor de K : "))

# calcular o polinomio
#
polinomio = fatorial(valorN) / (fatorial(valorK) * fatorial(valorN - valorK))

# exibir o resultado
#
print("o valor do polinomio eh : ", polinomio)