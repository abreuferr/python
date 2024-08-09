#!/usr/local/bin/python3

# variavel
#
peso = 78
altura = 1.81

# calcular o imc da pessoa
# varival do tipo float
#
imcFloat = peso / (altura ** 2)
textFloat = "o IMC é (ponto flutuante) :"

# conversao do tipo float para o tipo inteiro
#
imcInteiro = int(imcFloat)
textInt = "o IMC é (inteiro) : "

# conversao do tipo float para o tipo string
#
imcString = str(imcFloat)
textString = "o IMC é (srting) : "

# calcular o tamanho da string icmFloat
#
icmLen = len(textString)

# exibir o resiltado do imc da pessoa
#
print(textFloat, imcFloat)
print(textInt, imcInteiro)
print(textString, imcString)
print("O tamanho da string textString é : ", icmLen)