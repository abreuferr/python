import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
n_bolinhas = 20000   # quantas "bolinhas"
n_pinos = 30         # quantas decisões (linhas de pinos)

# Cada bolinha faz n_pinos decisões 0/1; soma = canal final
canais = np.random.randint(0, 2, size=(n_bolinhas, n_pinos)).sum(axis=1)

plt.figure()
plt.hist(canais, bins=range(n_pinos + 2), density=True, edgecolor="black")
plt.title("Simulação da Curva de Galton (Galton board)")
plt.xlabel("Canal final (nº de passos para a direita)")
plt.ylabel("Densidade")
plt.show()