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
    # inicializando variavel
    contador_a = 1
    contador_b = 1
    contador_c = 1

    # inicializando array
    array_e_raiz = []

    # varrer todas as possibilidades possivel de se formar um
    # triangulo cˆ2 = aˆ2 + bˆ2
    while contador_c <= numero:
        while contador_a <= numero:
            while contador_b <= numero:
                # verifica se os numeros forma um triangulo aristotelico
                e_raiz = e_hipotenusa(contador_a,contador_b,contador_c)
                if e_raiz != None:
                    # armazenar os valores obtidos no array "array_e_raiz"
                    array_e_raiz.append(e_raiz)
                
                contador_b += 1
            
            contador_b = 1
            contador_a += 1

        contador_a = 1
        contador_c += 1

    # eliminar valores duplicados presentes no array "array_e_raiz"
    total_e_raiz = []
    for i in array_e_raiz:
        if i not in total_e_raiz:
            total_e_raiz.append(i)
    
    # soma de todos os elementros do array "total_e_raiz"
    total = sum(total_e_raiz)
    return total

def e_hipotenusa(contador_A, contador_B, contador_C):
    # inicializa variavel
    E_raiz = 0

    # vairifica se eh um triangulo pitagorico
    if math.pow(contador_C,2) == math.pow(contador_A,2) + math.pow(contador_B,2):
        E_raiz = contador_C
        return E_raiz # se eh raiz, retorna com o valor
    
    return # se nao eh raiz, retorna zero

# main()
numero = int(input("insira um numero(n) inteiro positivo : "))
soma_hipotenusas(numero)