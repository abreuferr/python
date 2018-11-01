# autor : caio abreu ferreira
# objetivo : estudo sobre laco de repeticao utilizando o comando WHILE

# variavel
#
contador = 0

# inserindo os dados
#
valorBase = int(input("Favor inserir o valor da base : "))
valorExpoente = int(input("Favor inserir o valor do expoente : "))

while contador < valorExpoente:
    print(valorBase ** contador)
    contador += 1