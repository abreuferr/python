# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : inverter a ordem de uma sequencia de numeros

# main()

# array utilizado para armazenar os dados inseridos
lista = []

# inicializando variavel
digito = 1
contador = 0

while digito != 0:
    digito = int(input("Digite um número: "))
    # nao inserir o ZERO no array
    if digito != 0:
        lista.append(digito)

# inverter a ordem do array com os dados
lista.reverse()

while contador != len(lista):
    print(lista[contador], end='\n')
    contador += 1