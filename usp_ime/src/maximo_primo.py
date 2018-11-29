# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : exibir os numeros primos em um determinado intervalo.

# funcao primo
#
def primo(numero):
    fator = 2
    while numero % fator != 0 and fator < numero/2:
        fator += 1
    
    if numero % fator == 0:
        return False
    else:
        return True

# main()
#
limite = int(input("limite maximo : "))

# variavel
#
numero = 2

while numero < limite:
    if primo(numero):
        print(numero, end = ", ")
    numero += 1