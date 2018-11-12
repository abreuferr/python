# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre string

# variavel do tipo string convertida para
# o tipo inteiro
#
dia = int(input("Insira o dia de hoje : "))

# variavel do tipo string
#
mes = input("Insira o mes atual : ")
mes_strip = mes.strip()
mes_maiusculo = mes.upper()
mes_minusculo = mes_maiusculo.lower()
mes_capitalize = mes.capitalize()
mes_conta = mes.count("o")
mes_substituido = mes.replace(mes, "Dezembro")
mes_centralizado = mes.center(80)
mes_procura = mes.find("a")

# calculo
#
total = 3 * dia

# exibir resultados
#
print(mes[-1]) # exibir uma determinada letra do array
print(mes[3] * 3) # repetir uma determinada letra
print(mes_maiusculo) # converter para capslock
print(mes_minusculo) # reverter o capslock
print(mes_capitalize) # primeira letra Maiuscula
print(mes_strip) # remove espacos em branco
print(total) # multiplicacao
print(mes_conta) # quantas vezes a letra "o" aparece na palavra
print(mes_substituido) # substituir o mes digitado para Dezembro
print(mes_centralizado) # centralizar o texto em 80 caracteres
print(mes_procura) # primeira ocorrencia da letra "a"