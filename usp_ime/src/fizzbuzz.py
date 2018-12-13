# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : definir se um numero eh par ou impar
# OBS: // = parte inteira, % = resto
"""
Receba um número inteiro na entrada e imprima FizzBuzz
na saída se o número for divisível por 3 e por 5. 
Caso contrário, imprima o mesmo número que foi dado
na entrada.
"""

# inserir os dados
numero = int(input("Insira um númeroa ser verificado : "))

resto_3 = numero % 3
resto_5 = numero % 5

if (resto_3 == 0) and (resto_5 == 0):
    print("FizzBuzz")
else:
    print(numero)