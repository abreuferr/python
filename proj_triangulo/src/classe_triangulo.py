# definicao da classe Triangulo
class Triangulo:
    """ 
    classe Triangulo utilizado para manipular os lados de um triangulo (a, b, c)
    """
    
    # metodo __init__
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    # metodos a, b, c
    def a(self):
        return self.ladoA
    def b(self):
        return self.ladoB
    def c(self):
        return self.ladoC
    
    # metodo para calcular o perimetro
    def perimetro(self):
        return (self.ladoA + self.ladoB + self.ladoC)
    
    def testa_triangulo(self):
        assert self.ladoA == 3
        assert self.ladoB == 4
        assert self.ladoC == 5