# autor : caio abreu ferreira
# objetivo : calcular a soma de todos os digitos de um numero, 6532 = (6+5+3+2=16)

# variavel auxiliar
#
total = 0
subTotal = 0
novoNumero = 1

# coleta do numero a ser calculado
#
numero = int(input("Favor inserir o numero a ser calculado : "))

while novoNumero != 0:
    # obter o ultimo digito do numero
    #
    subTotal = numero % 10
    
    # remover o ultimo digito do numero
    #
    novoNumero = numero // 10
    
    # calcular a soma dos digitos
    #
    total = total + subTotal

    # o novo numero a ser calculado 
    #
    numero = novoNumero

print("O resultado da soma dos digitos é : ", total)
