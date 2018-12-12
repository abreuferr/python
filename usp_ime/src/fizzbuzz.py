# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : definir se um numero eh par ou impar
# OBS: // = parte inteira, % = resto

# inserir os dados
numero = int(input("Insira um númeroa ser verificado "))

resto_3 = numero % 3
resto_5 = numero % 5

if numero <= 0:
    print("FizzBuzz")
else:
    if (resto_3 == 0) and (resto_5 == 0):
        print("FizzBuzz")
    else:
        print(numero)