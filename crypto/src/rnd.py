# importando a bibliotecas
import random, time

# sera exibindo um numero aleatorio
print(random.randrange(1000000, 9999999))

# a semente sera gerada baseada no horario atual. 
# nao eh muito seguro utilizar essa tecnica pois
# se eh possivel saber o horario em que o aplicativo
# foi executado, sera possivel predizer o número
# que foi gerado.
random.seed(time.time())
# randrange() recebe inteiros; 10**n evita a conversão para float.
r1 = random.randrange(10**49, 10**50 - 1)

random.seed(time.time())
r2 = random.randrange(10**49, 10**50 - 1)

# exibindo os valores de R1 e R2.
print(r1)
print(r2)
