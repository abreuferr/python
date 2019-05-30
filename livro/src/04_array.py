# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre array

# definindo variavel
carros = ['ford', 'audi', 'mercedes', 'toyota']

# loop para varrer todas as celulas do array e exibir os conteudos das celulas.
for carro in carros:
    print(carro)

# ordenar o conteudo do array carros
carros_ordenados = sorted(carros)

# loop para varrer todas as celulas do array e exibir os conteudos das celulas.
for carro in carros_ordenados:
    # ativar a opcao de CapsLock.
    print("Fabricante de carro", carro.title())