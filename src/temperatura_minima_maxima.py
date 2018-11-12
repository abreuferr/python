# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : localiza a menor e maior temperatura dentro 
#               de um array

def minima_maxima(temperatura):
    print("A menor temperatura do mês foi : ", temperatura_minima(temperatura), "C. ")
    #print("A maior temperatura do mês foi : ", temperatura_maxima(temperatura), "C. ")

# funcao utilizada para localizar a menor temperatura
#
def temperatura_minima(temp):
    temperatura_minima = 0
    contador = 0
    while contador < len(temp):
        if temp[contador] < temperatura_minima:
            temperatura_minima = temps[contador]
        
        contador += 1
    
    return temperatura_minima

# main()
#
print("iniciando os testes ")

temp = [31, 21, 12, 3, 24, 15, 11, 27]

if temperatura_minima(temp) != 3: 
    print("valor errado para o array ", temp)

print("Finalizando os testes ")