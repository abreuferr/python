import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parâmetros ---
n_particles = 30     # número de partículas
n_steps = 800        # número de frames (passos no tempo)
dt = 1.0             # passo de tempo
D = 1.0              # "força" da difusão (coef. de difusão efetivo)
trail = 40           # tamanho do rastro (0 = sem rastro)

np.random.seed(0)    # reprodutibilidade (opcional)

# Em Browniano contínuo: var(incremento) = 2*D*dt por dimensão
sigma = np.sqrt(2 * D * dt)

# --- Simulação (pré-calcula tudo para animar suave) ---
# increments: (n_steps-1, n_particles, 3)
increments = np.random.normal(loc=0.0, scale=sigma, size=(n_steps - 1, n_particles, 3))

# positions: (n_steps, n_particles, 3)
positions = np.zeros((n_steps, n_particles, 3), dtype=float)
positions[1:] = np.cumsum(increments, axis=0)

# --- Plot 3D ---
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection="3d")
ax.set_title("Movimento Browniano 3D — várias partículas (animação)")

# limites iniciais (ajusta dinamicamente também)
max_range = np.percentile(np.abs(positions), 99)  # escala robusta
if max_range == 0:
    max_range = 1

ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_zlim(-max_range, max_range)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# pontos (uma coleção)
scat = ax.scatter([], [], [], s=25)

# rastros (um por partícula), opcional
lines = []
if trail > 0:
    for _ in range(n_particles):
        (ln,) = ax.plot([], [], [], linewidth=1, alpha=0.7)
        lines.append(ln)

# texto de frame
txt = ax.text2D(0.02, 0.95, "", transform=ax.transAxes)

def update(frame_idx: int):
    # posições no frame
    xyz = positions[frame_idx]  # (n_particles, 3)

    # atualizar scatter (matplotlib 3D usa _offsets3d)
    scat._offsets3d = (xyz[:, 0], xyz[:, 1], xyz[:, 2])

    # atualizar rastros
    if trail > 0:
        start = max(0, frame_idx - trail)
        segment = positions[start:frame_idx + 1]  # (len, n_particles, 3)
        for p, ln in enumerate(lines):
            ln.set_data(segment[:, p, 0], segment[:, p, 1])
            ln.set_3d_properties(segment[:, p, 2])

    txt.set_text(f"passo: {frame_idx+1}/{n_steps} | partículas: {n_particles} | D={D}")

    # (Opcional) ajustar limites dinamicamente se quiser:
    # cur = np.percentile(np.abs(positions[:frame_idx+1]), 99)
    # cur = max(cur, 1)
    # ax.set_xlim(-cur, cur); ax.set_ylim(-cur, cur); ax.set_zlim(-cur, cur)

    artists = [scat, txt] + lines
    return artists

ani = FuncAnimation(fig, update, frames=n_steps, interval=20, blit=False)
plt.show()