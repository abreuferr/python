# definicao da classe Veiculo
class Veiculo:
    # metodo __init__()
    def __init__(self, tipo, fabricante, cor, vel_max):
        self.tipo       = tipo # tipo do veiculo (carro/moto/caminhao)
        self.fabricante = fabricante # fabricante do veiculo (ford, honda)
        self.cor        = cor # cor do veiculo (vermelho, azul)
        self.vel_max    = vel_max  # velocidade maxima do veiculo