# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Em um numero digitado, verifica se o digito vizinho eh igual ou nao ao anterior

# variavel auxiliar
#
digitoAnterior = -1
digitoAtual = 0
novoNumero = 1

# coleta do numero a ser calculado
#
numero = int(input("Favor inserir o numero a ser verificado : "))

while novoNumero != 0:
    # obter os digitos do numero digitado
    #
    digitoAtual = numero % 10
    novoNumero = numero // 10

    # Verifica se o digito eh igial ao digito anterior
    #
    if digitoAtual == digitoAnterior:
        print("O numero ", digitoAtual, " eh igial ao digito anteior : ", digitoAnterior)

    digitoAnterior = digitoAtual

    # o novo numero a ser calculado 
    #
    numero = novoNumero