# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : equacao do segundo grau

# importando o modulo math
import math

# coleta dos dados
valorA = float(input("Favor inserir o valor de A : "))
valorB = float(input("Favor inserir o valor de B : "))
valorC = float(input("Favor inserir o valor de C : "))

# calcular o valor do delta
delta = math.pow(valorB, 2) - (4 * valorA*valorC)

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    valorX1 = (-valorB + math.sqrt(delta)) / (2 * valorA)
    print("a raiz desta equação é", valorX1)
else:
    valorX1 = (-valorB + math.sqrt(delta)) / (2 * valorA)
    valorX2 = (-valorB - math.sqrt(delta)) / (2 * valorA)
    if valorX1 < valorX2:
        print("as raízes da equação são", valorX1, "e", valorX2)
    else:
        print("as raízes da equação são", valorX2, "e", valorX1)