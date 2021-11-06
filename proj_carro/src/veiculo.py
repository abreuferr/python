# definicao da classe Veiculo
class Veiculo:
    # metodo __init__()
    def __init__(self, tipo, fabricante, cor, vel_max):
        self.tipo       = tipo # tipo do veiculo (carro/moto/caminhao)
        self.fabricante = fabricante # fabricante do veiculo (ford, honda)
        self.cor        = cor # cor do veiculo (vermelho, azul)
        self.vel_atual  = 0 # velocidade atual do carro
        self.vel_max    = vel_max  # velocidade maxima do veiculo
    
    # metodo velocidade()
    def velocidade(self, vel):
        self.vel_atual = vel
        if self.vel_atual > self.vel_max:
            self.vel_atual = self.vel_max
        self.imprimir()
    
    # metodo imprimir()
    def imprimir(self):
        if self.vel_atual == 0: # velocidade atual eh IGUAL a zero
            print( "Veiculo %s %s esta parado"%(self.tipo, self.fabricante))
        elif self.vel_atual < self.vel_max: # velocidade atual eh MENOR que a maxima
            print( "Veiculo tipo %s modelo %s na velocidade correta"%(self.tipo, self.fabricante) )
        else: # velocidade atual eh MAIOR que a maxima
            print( "Veiculo tipo %s modelo %s esta acima da velocidade"%(self.tipo, self.fabricante))