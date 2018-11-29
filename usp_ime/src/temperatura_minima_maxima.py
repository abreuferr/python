# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : dentro de varias temperaturas, encontrar a maior
#               temperatura e a menor temperatura.

# funcao utilizada para calcular a menor
# temperatura
#
def minima(temps):
    # inicializando variavel
    #
    min = temps[0]
    i = 1
    
    # varredura do array para encontrar a menor temperatura
    #
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

# funcao utilizada para calcular a maior
# temperatura
#
def maxima(temps):
    # inicializando variavel
    #
    max = temps[0]
    i = 1
    
    # varredura do array para encontrar 
    # a menor temperatura
    #
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max

# main()

# array com as temperaturas a 
# serem processadas
#
temperaturas = [10, 2, 23, -5, 0, 44]

# impressao dos resultador 
#
print("A menor temperatura do mes foi : ", minima(temperaturas), "C. ")
print("A maior temperatura do mes foi : ", maxima(temperaturas), "C. ")