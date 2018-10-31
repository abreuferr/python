# autor : caio abreu ferreira
# objetivo : inserir o numero de segundos e calcular o numero de horas, minutos e segundos

# inserir a quantidade de segundos
#
segundosString = input("Inserir a quantidade de segundos : ")

# converter segundosString do tipo string para o tipo inteiro
#
segundosInteiro = int(segundosString)

# calcular o numero de horas
#
# // = pegar somente a parte inteira
#
totalHora = segundosInteiro // 3600

# calcular o numero de minutos
#
# %  = pegar somente o resto
#
segundosRestante = segundosInteiro % 3600
totalMinutos = segundosRestante // 60

# calcular o numero de segundos
#
segundosFinal = segundosRestante % 60

# exibir o resultado
#
print(totalHora , "horas ", totalMinutos, " minutos ", segundosFinal, " segundos ")