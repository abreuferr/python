# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : conta quantos numeros primos existem em um 
#              determinado intervalo.

# funcao primo
#
def n_primo(limite):
    # inicializando variavel
    numero = 2
    total_primo = 0
    # verificar se o numero eh primo ou nao
    while numero <= limite:
        if primo(numero):
            total_primo += 1
        numero += 1
    # retornar com o total de numeros primos
    print(total_primo)
    return total_primo

# verificar se o numero eh primo ou nao
def primo(numero):
    fator = 2
    while numero % fator != 0 and fator < numero/2:
        fator += 1
    
    if numero % fator == 0:
        return False
    else:
        return True

# main()
limite = int(input("limite maximo : "))
n_primos = n_primo(limite)
print("o numero de primos nesse intervalo é de: ", n_primo)