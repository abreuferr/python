# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : 
"""
Escreva uma função soma_hipotenusas que receba como parâmetro 
um número inteiro positivo n e devolva a soma de todos os 
inteiros entre 1 e n que são comprimento da hipotenusa de 
algum triângulo retângulo com catetos inteiros.
"""
import math

def soma_hipotenusas(numero):
    e_hipotenusa(numero)

    return

def e_hipotenusa(numero):
    # inicializando variavel
    contador_a = 1
    contador_b = 1
    contador_c = 1

    while contador_c <= numero:
        while contador_a <= numero:
            while contador_b <= numero:
                if math.pow(contador_c,2) == math.pow(contador_a,2) + math.pow(contador_b,2):
                    print(contador_c,"=",contador_a,"+",contador_b)
                contador_b += 1
            contador_b = 1
            contador_a += 1
        contador_a = 1
        contador_c += 1
    return

# main()
numero = int(input("insira um numero(n) inteiro positivo : "))
soma_hipotenusas(numero)