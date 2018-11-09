# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : localiza a menor e maior temperatura dentro 
#               de um array

def minima_maxima(temperatura):
    print("A menor temperatura do mês foi : ", temperatura_minima(temperatura), "C. ")
    #print("A maior temperatura do mês foi : ", temperatura_maxima(temperatura), "C. ")

# funcao utilizada para localizar a menor temperatura
#
def temperatura_minima(temps):
    temperatura_minima = 0
    contador = 0
    while contador < len(temp):
        if temp[contador] < temperatura_minima:
            temperatura_minima = temps[contador]
        
        contador += 1
    
    return temperatura_minima

# funcao utilizada para testar a funcao minima
#
def testa_minima():
    print("iniciando os testes ")
    temp = [0]
    if temperatura_minima (temp) != 0: 
        print("valor errado para o array ", temp)
    
    temp = [0, 0, 0, 0, 0, 0]
    if temperatura_minima (temp) != 0: 
        print("valor errado para o array ", temp)
    
    temp = [0, 1, 2, 3, 4, 5, 6, 7]
    if temperatura_minima (temp) != 0: 
        print("valor errado para o array ", temp)

    temp = [31, 21, 12, -3, 24, 15, 11, 27]
    if temperatura_minima (temp) != -3: 
        print("valor errado para o array ", temp)

    print("Finalizando os testes ")