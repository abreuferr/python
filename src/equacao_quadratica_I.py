# autor : caio abreu ferreira
# objetivo : calcular os valores de x em uma equacao do segundo grau (ax**2+bx+c=0)

# importando o modulo math
#
import math

# exibir o formato de uma equacao de segundo grau
#
print("axˆ2+bx+c=0")

# coleta dos dados
#
valorA = float(input("Favor inserir o valor de A : "))
valorB = float(input("Favor inserir o valor de B : "))
valorC = float(input("Favor inserir o valor de C : "))

# calcular o valor do delta
#
delta = (valorB ** 2) - (4 * valorA*valorC)


# valor do dlta igual a zero
#
if delta == 0:
    # calcular o valor de X1 e exibir o resultado
    #
    valorX1 = (-valorB + math.sqrt(delta)) / (2 * valorA)
    print("A única raiz é : ", valorX1)

# valor do delta é maior que zero
#
elif delta < 0:
    print("Esta equacao nao possui raizes reais")

# valor do delta é maior que zero
#
else:
    # calcular os valores de X1 e X2 e exibir o resultado
    #
    valorX1 = (-valorB + math.sqrt(delta)) / (2 * valorA)
    valorX2 = (-valorB - math.sqrt(delta)) / (2 * valorA)
    print("Valor de x1 é : ", valorX1)
    print("Valor de x2 é : ", valorX2)