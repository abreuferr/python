# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : programa Hello World.

# array para estudo.
carros = ['audi', 'Bmw', 'subaru', 'toyota']

# varrer o array.
for carro in carros:
    # condicao e normalizacao da entrada.
    if carro.lower() == 'bmw':
        print(carro.upper())
    # caso contrario.
    else:
        print(carro.title())