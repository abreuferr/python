# autor : caio abreu ferreira
# objetivo : calcular os valores de x em uma equacao do segundo grau (ax**2+bx+c=0)

import math

class Bhaskara:
    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c

    def main(self):
        a_digitado = float(input("Favor inserir o valor de A : "))
        b_digitado = float(input("Favor inserir o valor de B : "))
        c_digitado = float(input("Favor inserir o valor de C : "))
        print(self.calcula_raizes(a_digitado, b_digitado, c_digitado))

    # funcao calcularx
    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)

        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2*a)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                # calcular o valor de X1 e X2 e retornar os valores
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2