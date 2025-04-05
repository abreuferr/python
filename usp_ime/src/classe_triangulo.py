# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : estudo sobre OOP em Python - exercicio
"""
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros 
correspondentes aos lados a, b e c de um triângulo.

A classe Triangulo também deve possuir um método perimetro, que não 
recebe parâmetros e devolve um valor inteiro correspondente ao perímetro 
do triângulo.

t = Triangulo(1, 1, 1) # deve atribuir uma referência para um triângulo de lados 1, 1 e 1 à variável t 
t.a # deve devolver o valor do lado a do triângulo
t.b # deve devolver o valor do lado b do triângulo
t.c # deve devolver o valor do lado c do triângulo

t.perimetro() # deve devolver um inteiro correspondente ao valor do perímetro do triângulo.
"""

# classe main()
def main():
    t = Triangulo(1, 1, 1)

# definicao da classe Triangulo
class Triangulo:

    # metodo __init__
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a  = lado_a
        self.lado_b  = lado_b
        self.lado_c  = lado_c

    # metodo perimetro()
    def perimetro(self):
        perimetro = lado_a + lado_b + lado_c

# main()
main()