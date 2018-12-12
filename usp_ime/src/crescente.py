# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : verificar se os numeros inseridos estao em ordem crescente

# declaracao das variaveis
decrescente = True
valor = 1

# inserir os numeros
primeiro_numero = int(input("digite o primeiro numero da sequencia : "))
segundo_numero = int(input("digite o segundo numero da sequencia : "))
terceiro_numero = int(input("digite o terceiro numero da sequencia : "))

# verificacao da ordem
if segundo_numero < primeiro_numero:
    print("não está em ordem crescente")
elif terceiro_numero < segundo_numero:
    print("não está em ordem crescente")
else:
    print("crescente")