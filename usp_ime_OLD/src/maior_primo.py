# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : encontrar o maior numero primo em uma faixa de numeros

# funcao maior_primo
def maior_primo(limite):
    numero = 2
    while numero <= limite:
        if primo(numero):
            maior_primo_encontrado = numero
            #print(numero, end = ", ")
        numero += 1
    return maior_primo_encontrado

# funcao primo
def primo(numero):
    fator = 2
    while numero % fator != 0 and fator < numero/2:
        fator += 1
    
    if numero % fator == 0:
        return False
    else:
        return True

# main()
limite = int(input("Digite um numero maior que 2 : "))
x = maior_primo(limite)
print(x)