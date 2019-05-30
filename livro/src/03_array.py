# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre array

# definindo variavel
frutas = ['abacate', 'pera', 'maca', 'limao']
carros = ['ford', 'audi', 'mercedes', 'toyota']
texto = "Minha fruta favorita eh"

# exibicao de um array.
print(frutas)

# exibicao do conteudo da primeira celula de um array.
print(frutas[0])

# exibicao do conteudo da ultima celula de um array.
print(frutas[-1]) 

# exibicao do conteudo da celula[2] de um array.
print(frutas[2])

# exibicao do conteudo da celula[2] de um array em modo CapsLock.
print(frutas[0].title())

# concatenando uma variavel do tipo string com uma celula de um array.
print(texto, frutas[1].title(),".")

# substituir o conteudo da celula frutas[1] por outro conteudo.
print(frutas)
frutas[1] = "caju"
print(frutas)

# inserir um novo dado no FINAL de um array atraves do metodo APPEND.
print(frutas)
frutas.append("laranja")
print(frutas)

# inserir um novo dado em uma POSICAO de um array - metodo INSERT.
print(frutas)
frutas.insert(1,"tangerina")
print(frutas)

# remover um dado em uma POSICAO de um array - metodo DEL.
print(frutas)
del frutas[3]
print(frutas)

# copiar o ultimo item de um array e colocar em uma variavel - metodo POP.
print(frutas)
ultima_fruta = frutas.pop()
print("O ultimo item da lista de frutas é a " + ultima_fruta.title() + ".")

# copiar um item de um array e colocar em uma variavel - metodo POP.
print(frutas)
terceira_fruta = frutas.pop(2)
print("O terceiro item da lista de frutas é a fruta " + terceira_fruta.title() + ".")

# remover a fruta "tangerina" de um array - metodo REMOVE.
print(frutas)
fruta_removida = "tangerina"
frutas.remove(fruta_removida)
print(frutas)

# ordenar um array - metodo SORT
# ordenado de forma PERMANENTE.
print(carros)
carros.sort()
print(carros)

# ordenar de forma REVERSA um array - metodo SORT
# ordenado de forma PERMANENTE.
print(carros)
carros.sort(reverse=True)
print(carros)

# inicializa array
carros = ['fiat', 'audi', 'bmw', 'honda']

# ordenar de forma REVERSA um array - metodo SORTED
# ordenado de forma TEMPORARIA.
print(carros)
carros_ordenados = sorted(carros)
print(carros_ordenados)
print(carros)

# exibir os dados do array de forma inversa - REVERSE
print(carros)
carros.reverse()
print(carros)

# exibir o tamanho do array - LEN
print(carros)
tamanho_carros = len(carros)
print(tamanho_carros)