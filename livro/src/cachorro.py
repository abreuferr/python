# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : estudo sobre OOP em Python - livro sobre Python

# metodo main()
def main():
    # nome_da_instancia = nome_do_objeto(valor_atributo1, valor_atributo2)
    cachorro_val = Cachorro('tula', 1)
    cachorro_mariana = Cachorro('malu', 5)

# definicao da classe Cachorro
class Cachorro:
    # metodo init e 03 parametros.
    def __init__(self, nome, idade):
        # iniciaiza os atributos do cachorro.
        self.nome = nome
        self.idade = idade
    
    # metodo sentar()
    # metodo que simula um cachorro sentado.
    def sentar(self):
        print(self.nome.titulo() + "agora esta sentado")

    # metodo rolar()
    # metodo que simula um cachorro rolando.
    def rolar(self):
        print(self.nome.titulo() + "agora esta rolando")

# main()
main()
