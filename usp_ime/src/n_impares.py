# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : exibir os numeros impares entre 1 e um determinado valor
# OBS: 5 = 1 3 5 7 9

# variavel auxiliar
numero = 1

# inserir o valor de n
contador = int(input("Digite o valor de n:"))

while (contador != 0):
    total = numero % 2 
    if total != 0: # verificar se eh impar
        print(numero) # exibe o resultado
        contador -= 1

    numero += 1
    total = numero