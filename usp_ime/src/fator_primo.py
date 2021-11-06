# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : calcula os fatores primos e multiplicades de um numero
#               1000 = 2ˆ3 * 5ˆ3

# declaracao de variavel
#
fator = 2
multiplicidade = 0

# main()
#
numero = int(input("Digite um numero inteiro maior que 1 : "))

while numero > 1:
    while numero % fator == 0:
        multiplicidade += 1
        numero = numero / fator
    
    if multiplicidade > 0:
        print("fator : ", fator, "multiplicidade : ", multiplicidade)
    
    fator += 1
    multiplicidade = 0