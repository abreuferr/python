# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : exibir qual eh o maior numero entre 3 numeros
# OBS :
"""
Reescreva a funcao 'maximo' que devolve o maior valor dentre
dois inteiros recebidos, para que ela passe a receber 3 valores
inteiros como parametros e devolva o maior dentre eles.
maximo(30,14,10) deve devolver 30
maximo(0,-1, 1) deve devolver 1
"""

# funcao maximo
def maximo(numero_1,numero_2,numero_3):
    resto_3 = numero % 3
    resto_5 = numero % 5

    if (resto_3 == 0) and (resto_5 != 0):
        msg = "Fizz"
        return msg
    elif (resto_3 != 0) and (resto_5 == 0):
        msg = "Buzz"
        return msg
    elif (resto_3 == 0) and (resto_5 == 0):
        msg = "FizzBuzz"
        return msg
    else:
        return numero

# main()

# inserir os dados
numero_1 = int(input("Insira o primeiro numero : "))
numero_2 = int(input("Insira o segundo numero : "))
numero_3 = int(input("Insira o terceiro numero : "))
print(maximo(numero_1,numero_2,numero_3))