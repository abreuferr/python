import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# Parâmetros
# -----------------------------
n_pinos = 14
n_bolinhas = 250
frames_por_nivel = 6
spawn_rate = 4
jitter_x = 0.03

# Geometria do histograma/empilhamento
dy_stack = 0.18          # espaçamento vertical entre bolinhas empilhadas
base_y = -n_pinos - 2.0  # "chão" do histograma
bin_width = 1.0          # largura efetiva do bin (em x)

rng = np.random.default_rng(42)

# -----------------------------
# Pinos (triângulo)
# -----------------------------
pinos_x, pinos_y = [], []
for y in range(n_pinos):
    for x in range(y + 1):
        pinos_x.append(x - y / 2)
        pinos_y.append(-y)

# -----------------------------
# Estado das bolinhas
# -----------------------------
INATIVA = 9999.0

x = np.zeros(n_bolinhas, dtype=float)
y = np.ones(n_bolinhas, dtype=float) * INATIVA
nivel = np.zeros(n_bolinhas, dtype=int)
settled = np.zeros(n_bolinhas, dtype=bool)

# decisões: -0.5 (esq) ou +0.5 (dir)
decisoes = rng.choice([-0.5, 0.5], size=(n_bolinhas, n_pinos))

# bin final (quantas vezes foi pra direita)
bins = (decisoes == 0.5).sum(axis=1)  # 0..n_pinos

# contagem de empilhamento por bin
stack_count = np.zeros(n_pinos + 1, dtype=int)

# quantas bolinhas já foram liberadas
liberadas = 0

# -----------------------------
# Plot
# -----------------------------
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.axis("off")

# limites (aumenta um pouco pra caber o histograma)
ax.set_xlim(-n_pinos, n_pinos)
ax.set_ylim(base_y - 2, 2)

# desenha pinos
ax.scatter(pinos_x, pinos_y, s=18, zorder=1)

# desenha “marcas” do histograma (linhas verticais leves)
# (só pra referência visual)
for b in range(n_pinos + 1):
    bx = (b - n_pinos / 2) * bin_width
    ax.plot([bx, bx], [base_y - 0.2, base_y + 0.2], linewidth=1)

# bolinhas (scatter)
sc = ax.scatter([], [], s=22, zorder=3)

# -----------------------------
# Funções auxiliares
# -----------------------------
def bin_center_x(b):
    # centraliza o bin de 0..n_pinos em torno do x=0
    return (b - n_pinos / 2) * bin_width

def settle_ball(i):
    """Encaixa a bolinha i na pilha do bin final."""
    b = bins[i]
    cx = bin_center_x(b)

    # altura na pilha atual
    k = stack_count[b]
    stack_count[b] += 1

    # pequeno jitter horizontal pra parecer “cheio” sem sobrepor perfeito
    x[i] = cx + rng.normal(0.0, 0.06)
    y[i] = base_y + k * dy_stack
    settled[i] = True

# -----------------------------
# Update da animação
# -----------------------------
def update(frame):
    global liberadas

    # 1) libera bolinhas aos poucos
    if liberadas < n_bolinhas:
        n_new = min(spawn_rate, n_bolinhas - liberadas)
        idx = np.arange(liberadas, liberadas + n_new)

        x[idx] = rng.normal(0.0, jitter_x, size=n_new)
        y[idx] = 1.2
        nivel[idx] = 0
        settled[idx] = False

        liberadas += n_new

    # 2) movimenta bolinhas ativas (que ainda não assentaram)
    ativos = np.where((y < INATIVA) & (~settled))[0]
    for i in ativos:
        if nivel[i] < n_pinos:
            # “queda” dentro do nível
            y[i] -= 1 / frames_por_nivel
            x[i] += decisoes[i, nivel[i]] / frames_por_nivel

            # ao terminar o nível, avança pro próximo
            if frame % frames_por_nivel == frames_por_nivel - 1:
                nivel[i] += 1
        else:
            # já passou por todos os pinos: cai até o chão e então encaixa
            y[i] -= 1 / frames_por_nivel
            if y[i] <= base_y:
                settle_ball(i)

    # 3) desenha todas as bolinhas já liberadas (ativas + assentadas)
    visiveis = np.where(y < INATIVA)[0]
    sc.set_offsets(np.c_[x[visiveis], y[visiveis]])
    return (sc,)

ani = FuncAnimation(fig, update, interval=35, blit=True)
plt.show()
