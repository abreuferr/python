# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : definir se um numero eh par ou impar
# OBS: // = parte inteira, % = resto

# inserir os dados
numero = int(input("Insira um númeroa ser verificado"))

resto = numero % 3

if resto == 0:
    print("Fizz")
else:
    print(numero)