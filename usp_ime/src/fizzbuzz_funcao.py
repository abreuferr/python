# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : definir se um numero eh divisivel por 3 ou 5
# OBS: // = parte inteira, % = resto
"""
Escreva a funcao fizzbuzz que recebe como parametro um numero 
inteiro e devolve: 

- 'Fizz' se o numero for divisivel por 3 e nao for divisivel por 5;
- 'Buzz' se o numero for divisivel por 5 e nao for divisivel por 3;
- 'FizzBuzz' se o numero for divisivel por 3 e por 5;
- exibir o numero se nao for divisivel por 3 e por 5
"""

# funcao fizzbuzz
def fizzbuzz(numero):
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
numero = int(input("Insira o numero a ser verificado : "))
print(fizzbuzz(numero))