# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : exibir as dezenas de um numero
# OBS1 : // = inteiro, % = resto
# OBS2 : 78615 = 1, 2 = 0

# inserir as notas
numero = int(input("Digite um número inteiro: "))

# calcular a media
dezena = (numero)%100
digito = (dezena)//10

# exibir o digito da dezena
print("O dígito das dezenas é", digito)