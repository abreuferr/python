# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre array

# contruindo o array
#
temperaturaCelsius = [23, 12, 42, 5, 9]

# exibir o conteudo de todas as celulas do
# array
#
print(temperaturaCelsius)

# exibir o conteudo de uma celula do array
#
print(temperaturaCelsius[1])

# exibe a quantidade de celulas um determinado
# array possui
#
print(len(temperaturaCelsius))

# exibe o tipo do conteudo de uma celula do array
# nesse exemplo, o retorno é do tipo int.
#
print(type(temperaturaCelsius[2]))

# adicionar um novo dado ao array
#
temperaturaCelsius.append(-9)
print(temperaturaCelsius)

# alterar o conteudo de uma determinada celula
#
print(temperaturaCelsius[3])
temperaturaCelsius[3] = 15
print(temperaturaCelsius[3])

# outra forma de alterar o conteudo de uma celula
# do array. Neste caso, é a última celula do array
#
print(temperaturaCelsius[-1])
temperaturaCelsius[-1] = temperaturaCelsius[-1] + 3
print(temperaturaCelsius[-1])