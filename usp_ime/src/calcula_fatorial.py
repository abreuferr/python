# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calcula o fatorial de um numero digitado pelo usuario

# funcao fatorial
#
def fatorial(valor):
    valorFatorial = 1
    while valor > 1:
        valorFatorial = valorFatorial * valor
        valor -= 1
    return valorFatorial

# main()
#
numero = int(input("inserir um numero inteiro e positivo ou zero : "))

while numero >= 0:
    resultado = fatorial(numero)
    print(resultado)
    numero = int(input("inserir um numero inteiro e positivo ou zero : "))