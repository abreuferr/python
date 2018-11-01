# autor : caio abreu ferreira
# objetivo : verificar se a ondem de numeros digitados esta em ordem decrescente

# declaracao das variaveis
#
decrescente = True
valor = 1

# inserir o primerio numero da sequencia
#
anterior = int(input("digite o primeiro numero da sequencia : "))

# executar enquanto o usuario nao digitar 0(zero) na entrada
#
while valor != 0 and decrescente:
    # inserir o(s) proximo(s) valor(es) da sequencia
    #
    valor = int(input("digite o proximo numero da sequencia : "))

    # comparar o valor atual com o valor anterior
    #
    if valor > anterior:
        # o valor inserido eh maior que o anterior
        #
        decrescente = False
    
    # o valor inserido eh menor que o valor anterior
    #
    anterior = valor

# decrescente = True
#
if decrescente:
    print("a sequencia esta em ordem decrescente ")
# decrescente = False
#
else:
    print("a sequencia nao esta em ordem decrescente")