# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - parte 2 - metodo __init__

class carro:
    # método __init__(atributos)
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

# objeto carro
# atributos ferrari, 1980 e vermelho
carro_do_meu_avo = carro("Ferrari", 1980, "vermelho")

print(carro_do_meu_avo.cor)