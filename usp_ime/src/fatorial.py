# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Esse programa tem como finalidade a de testar o Pytest
# OBS: 5! = 120

# inicializando variavel
valor_fatorial = 1

# inserir o dado
numero = int(input("Digite o valor de n:"))

while (numero > 1):
    valor_fatorial = valor_fatorial * numero
    numero = numero - 1

# exibir o valor do fatorial
print(valor_fatorial)