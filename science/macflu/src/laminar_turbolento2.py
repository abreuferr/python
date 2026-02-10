import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações da simulação
n_particles = 15
frames = 100
x_limit = 10

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
plt.subplots_adjust(hspace=0.4)

# Setup do gráfico Laminar
ax1.set_xlim(0, x_limit)
ax1.set_ylim(-1, n_particles)
ax1.set_title("Fluxo Laminar (Ordenado)")
lines_lam = [ax1.plot([], [], 'b-', alpha=0.6)[0] for _ in range(n_particles)]
dots_lam = [ax1.plot([], [], 'bo')[0] for _ in range(n_particles)]

# Setup do gráfico Turbulento
ax2.set_xlim(0, x_limit)
ax2.set_ylim(-1, n_particles)
ax2.set_title("Fluxo Turbulento (Caótico)")
lines_turb = [ax2.plot([], [], 'r-', alpha=0.4)[0] for _ in range(n_particles)]
dots_turb = [ax2.plot([], [], 'ro')[0] for _ in range(n_particles)]

# Dados das trajetórias
x_data = np.linspace(0, x_limit, frames)
y_base = np.arange(n_particles)

def update(frame):
    for i in range(n_particles):
        # Laminar: y constante
        curr_x = x_data[:frame]
        curr_y_lam = np.full_like(curr_x, y_base[i])
        lines_lam[i].set_data(curr_x, curr_y_lam)
        if frame > 0: dots_lam[i].set_data([curr_x[-1]], [curr_y_lam[-1]])

        # Turbulento: y com ruído aleatório (Random Walk)
        noise = np.cumsum(np.random.normal(0, 0.08, frame)) 
        curr_y_turb = y_base[i] + noise
        lines_turb[i].set_data(curr_x, curr_y_turb)
        if frame > 0: dots_turb[i].set_data([curr_x[-1]], [curr_y_turb[-1]])
    
    return lines_lam + dots_lam + lines_turb + dots_turb

ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
plt.show()