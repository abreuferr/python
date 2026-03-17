import numpy as np
import matplotlib.pyplot as plt

# número de passos
n = 5000

# arrays de posição
x = np.zeros(n)
y = np.zeros(n)

# gerar passos aleatórios
for i in range(1, n):
    dx = np.random.normal(0, 1)  # passo em x
    dy = np.random.normal(0, 1)  # passo em y
    
    x[i] = x[i-1] + dx
    y[i] = y[i-1] + dy

# plot da trajetória
plt.figure(figsize=(8,6))
plt.plot(x, y, linewidth=1)
plt.scatter(x[0], y[0], color='green', label='Início')
plt.scatter(x[-1], y[-1], color='red', label='Fim')

plt.title("Simulação de Movimento Browniano (2D)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

plt.show()