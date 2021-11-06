# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : funcao para calcular o maior entre dois numeros

# funcao maximo
def maximo(numero_1, numero_2):
    if numero_1 > numero_2:
        return numero_1
    else:
        return numero_2

numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))

print(maximo(numero_1,numero_2))