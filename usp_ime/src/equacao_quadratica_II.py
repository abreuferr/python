# autor : caio abreu ferreira
# objetivo : calcular os valores de x em uma equacao do segundo grau (ax**2+bx+c=0)

# importando o modulo math
#
import math

# funcao delta
#
def delta(valorA, valorB, valorC):
    # calcular o valor do delta e retornar o valor
    #
    valorDelta = (valorB ** 2) - (4 * valorA*valorC)
    return valorDelta

# funcao calcularx
#
def calcularx(valorA, valorB, valorDelta):
    # calcular o valor de X1 e X2 e retornar os valores
    #
    valorX1 = (-valorB + math.sqrt(valorDelta)) / (2 * valorA)
    valorX2 = (-valorB - math.sqrt(valorDelta)) / (2 * valorA)
    return valorX1, valorX2

# exibir o formato de uma equacao de segundo grau
#
print("axˆ2+bx+c=0")

# coleta dos dados
#
valorA = float(input("Favor inserir o valor de A : "))
valorB = float(input("Favor inserir o valor de B : "))
valorC = float(input("Favor inserir o valor de C : "))

# calcular o valor do delta atraves da funcao DELTA
#
valorDelta = delta(valorA, valorB, valorC)

# valor do delta igual a zero
#
if valorDelta == 0:
    # calcular o valor de X1 e exibir o resultado
    #
    valorX1 = calcularx(valorA, valorB, valorDelta)
    print("A única raiz é : ", valorX1)

# valor do delta é menor que zero
#
elif valorDelta < 0:
    print("Esta equacao nao possui raizes reais")

# valor do delta é maior que zero
#
else:
    # calcular os valores de X1 e X2 e exibir o resultado
    #
    valorX1 = calcularx(valorA, valorB, valorDelta)
    valorX2 = calcularx(valorA, valorB, valorDelta)
    print("Valor de x1 é : ", valorX1)
    print("Valor de x2 é : ", valorX2)