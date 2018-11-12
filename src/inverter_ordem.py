# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : o usuario ira inserir dados em um array e o programa
#               ira inverter a ordem dos numeros digitados.

# definir variavel
#
dado = 1

# criacao do array numero
#
numero = []

# coleta de dados
#
dado = float(input("inserir o numero, 0 para sair : "))

while dado != 0:
    # armazenando o dado no arrya numero
    #
    numero.append(dado)
    
    # coleta de dados
    #
    dado = float(input("inserir o numero, 0 para sair : "))

# 3xibe o conteudo do array
#
print(numero)

# tamanho do array -1
#
tamanhoArray = len(numero) - 1

# inverte a ordem do conteudo do array
#
while tamanhoArray >= 0:
    print(numero[tamanhoArray], end=", ")
    tamanhoArray -= 1