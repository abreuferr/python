# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : verificar se o numero é primo ou não.

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
numero = int(input("Digite um numero inteiro maior que 2 : "))

while numero > 2:
    if primo(numero):
        print("O numero ", numero, " é primo ")
    else:
        print("O numero ", numero, " NÃO é primo ")
    
    numero = int(input("Digite um numero inteiro maior que 1 : "))