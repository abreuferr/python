# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre estrutura de repeticao FOR com RANGE

# contruindo o array
#
temperaturaCelsius = [23, 12, 42, 5, 9, 32, -1, 51]

# varrer todo o array
#
for temperatura in range(len(temperaturaCelsius)):
    print("Temperatura : ", temperaturaCelsius[temperatura] * 2)

# definir o inicio e o final da varredura
#
for temperatura in range(2, 4):
    print("Temperatura : ", temperaturaCelsius[temperatura])

# definir o inicio, final e o passo da varredura
#
for temperatura in range(1, 6, 2):
    print("Temperatura : ", temperaturaCelsius[temperatura])

# armazenar o ranche em uma variavel
#
pares = range(0, 20, 2)
for i in pares:
    print("Numero : ", i)