# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : calcular a soma de todos os digitos de um numero
# OBS: 6532 = (6+5+3+2=16)


# inicializando vaviavel
total = 0
subTotal = 0
novoNumero = 1

# coleta do numero a ser calculado
numero = int(input("Digite um número inteiro:"))

while novoNumero != 0:
    # obter o ultimo digito do numero
    subTotal = numero % 10
    
    # remover o ultimo digito do numero
    novoNumero = numero // 10
    
    # calcular a soma dos digitos
    total = total + subTotal

    # o novo numero a ser calculado 
    numero = novoNumero

# exibe o resultado
print(total)