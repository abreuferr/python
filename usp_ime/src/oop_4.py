# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - parte 4

# classe Veiculo
class Veiculo():
    # metodo __init__
    def __init__(self, tipo, marca, cor, vel_max):
        self.tipo = tipo
        self.marca = marca
        self.cor = cor
        self.vel_atual = 0
        self.vel_max = vel_max
    
    # metodo utilizado para comparar
    # a velocidade atual com a velocidade
    # maxima.
    def acelera(self, vel_atual):
        self.vel_atual = vel_atual
        if self.vel_atual > self.vel_max:
            self.vel_atual = self.vel_max
        self.imprimir()
    
    # metodo utilizado para exibir uma
    # mensagem dependendo da velocidade
    # atual do carro.
    def imprimir(self):
        if self.vel_atual < self.vel_max:
            print("%s - velocidade atual eh MENOR que a velocidade maxima"%(self.marca))
        else:
            print("%s - velocidade atual eh MAIOR que a velocidade maxima"%(self.marca))

# classe main()
def main():
    # objetos e suas caracteristicas
    veiculo1 = Veiculo("carro", "ferrari", "vermelho", 240)
    veiculo2 = Veiculo("caminhao", "ford", "azul", 200 )

    # imprimir as caracteristicas dos veiculos
    print("%s %s %s %d"%(veiculo1.tipo, veiculo1.marca, veiculo1.cor, veiculo1.vel_max))
    print("%s %s %s %d"%(veiculo2.tipo, veiculo2.marca, veiculo2.cor, veiculo2.vel_max))

    # chama acelera() como parametro a velocidade atual do veiculo
    veiculo1.acelera(260)
    veiculo2.acelera(180)

# main()
main()