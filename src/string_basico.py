# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre string

# variavel do tipo string convertida para
# o tipo inteiro
#
dia = int(input("Insira o dia de hoje : "))

# variavel do tipo string
#
mes = input("Insira o mes atual : ")
mes_maiusculo = mes.upper() # primeira letra maiuscula
mes_minusculo = mes_maiusculo.lower() # todas as letras minusculas
mes_capitalize = mes.capitalize() # primeira letra Maiuscula
mes_strip = mes.strip() # remove espacos em branco no comeco e final da strig
mes_conta = mes.count("o") # numero de vezes que aparece uma letra
mes_substituido = mes.replace(mes, "Dezembro") # substituir o conteudo por outro
mes_centralizado = mes.center(80) # centralizar a string
mes_procura = mes.find("a") # procurar por uma letra
mes_comprimento = len(mes) # exibir o tamanho da string

# exibir resultados
#
print(mes[-1]) # exibir um determinado caractere do array
print(mes[3] * 3) # repetir um determinada caractere N vezes
print(mes_maiusculo)
print(mes_minusculo)
print(mes_capitalize)
print(mes_strip) 
print(3 * dia)
print(mes_conta)
print(mes_substituido)
print(mes_centralizado)
print(mes_procura)

# exibir partes da string
print(mes[:4])
print(mes[1:])
print(mes[2:4])