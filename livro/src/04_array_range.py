# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre array - funcao RANGE()

# definindo variavel

# loop para gerar valores.
for valor in range(1,10):
    print(valor)

# atraves da funcao LIST() eh possivel converter os numeros
# em uma lista.
numeros = list(range(1,6))
print(numeros)

# range(INICIO,FIM,INCREMENTO)
numeros = list(range(3,30,3))
print(numeros)

# array para salvar dados, quadrados
quadrados = []
# loop para gerar valores de 1 ate 6
for valor in range(1,11):
    # calcular o quadrado de cada numero gerado.
    quadrado = valor ** 3
    # adicionar os valores calculados no array quadrados[]
    quadrados.append(quadrado)
# exibir o conteudo do array quadrados[]
print(quadrados)

# do array quadrados[], serao exibido somente alguns dados.
# array[origem:quantidade]
# origem[1] e final[3].
print(quadrados[1:3])

# do array quadrados[], serao exibido somente alguns dados.
# array[origem:quantidade]
# origem[0] e final[4].
print(quadrados[:4])

# do array quadrados[], serao exibido somente alguns dados.
# array[origem:quantidade]
# origem[0] e final[fim_array].
print(quadrados[2:])

# do array quadrados[], serao exibido os 03 ultimos registros.
print(quadrados[-3:])

# array utilizado pelo exercicio
nomes = ['caio', 'marcos', 'clovis', 'ana', 'nic']
# ler os nomes dos 03 primeiros usuarios do array
for nome in nomes[0:3]:
    # exibir os nome em modo CapsLock. 
    print(nome.title())

# array utilizado pelo exercicio
nomes = ['caio', 'marcos', 'clovis', 'ana', 'nic']
# copiar o conteudo do array nomes[] para o array familia[]
familia = nomes[:]
print(nomes)
print(familia)

# adicionar registros nos array[]
nomes.append('pedro')
familia.append('matheus')
print(nomes)
print(familia)
