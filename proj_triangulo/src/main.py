# Do arquivo classe_triangulo.py, importar a classe Triangulo
from classe_triangulo import Triangulo

# classe main()
def main():

    # chamando a classe Triangulo(a, b, c)
    # e armazenando na variavel "t"
    t = Triangulo(3,4,5)

    # calcular o perimetro
    print(t.perimetro())

# main()
main()