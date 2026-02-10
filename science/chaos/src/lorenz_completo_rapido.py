"""
Versão Rápida - Atrator de Lorenz com Trajetória Completa
Execute este arquivo para ver a animação sem apagar a trajetória!
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def lorenz(x, y, z, sigma=10, rho=28, beta=8/3):
    """Equações do sistema de Lorenz"""
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

def simular_lorenz(x0=0, y0=1, z0=1.05, dt=0.01, num_passos=5000):
    """Simula o sistema de Lorenz"""
    xs = np.zeros(num_passos)
    ys = np.zeros(num_passos)
    zs = np.zeros(num_passos)
    
    xs[0], ys[0], zs[0] = x0, y0, z0
    
    for i in range(num_passos - 1):
        dx, dy, dz = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + dx * dt
        ys[i + 1] = ys[i] + dy * dt
        zs[i + 1] = zs[i] + dz * dt
    
    return xs, ys, zs

# Gerar dados
print("=" * 60)
print("ATRATOR DE LORENZ - TRAJETÓRIA COMPLETA")
print("=" * 60)
print("\n✨ Gerando trajetória...")
xs, ys, zs = simular_lorenz(num_passos=4000)
print(f"✓ {len(xs)} pontos gerados")

# Configurar animação
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Limites
margem = 5
ax.set_xlim([xs.min() - margem, xs.max() + margem])
ax.set_ylim([ys.min() - margem, ys.max() + margem])
ax.set_zlim([zs.min() - margem, zs.max() + margem])

# Labels
ax.set_xlabel('X', fontsize=12, labelpad=10)
ax.set_ylabel('Y', fontsize=12, labelpad=10)
ax.set_zlabel('Z', fontsize=12, labelpad=10)
ax.set_title('Atrator de Lorenz - Trajetória Crescente', 
             fontsize=16, fontweight='bold', pad=20)

# Elementos da animação
linha, = ax.plot([], [], [], 'b-', alpha=0.7, linewidth=2, label='Trajetória')
ponto, = ax.plot([], [], [], 'ro', markersize=12, markeredgecolor='darkred', 
                 markeredgewidth=2, label='Posição atual')

# Marcar ponto inicial
ax.scatter([xs[0]], [ys[0]], [zs[0]], color='lime', s=200, marker='*', 
          label='Início', edgecolors='darkgreen', linewidths=2, zorder=5)

# Texto informativo
texto = ax.text2D(0.02, 0.98, '', transform=ax.transAxes, 
                  fontsize=11, verticalalignment='top',
                  bbox=dict(boxstyle='round', facecolor='lightblue', 
                          alpha=0.8, edgecolor='navy'))

ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')

def init():
    """Inicializa animação"""
    linha.set_data([], [])
    linha.set_3d_properties([])
    ponto.set_data([], [])
    ponto.set_3d_properties([])
    return linha, ponto, texto

def update(frame):
    """Atualiza frame - a trajetória CRESCE sem apagar!"""
    # Desenha do início até o frame atual (trajetória completa crescente)
    linha.set_data(xs[:frame+1], ys[:frame+1])
    linha.set_3d_properties(zs[:frame+1])
    
    # Ponto atual
    ponto.set_data([xs[frame]], [ys[frame]])
    ponto.set_3d_properties([zs[frame]])
    
    # Informações
    tempo = frame * 0.01
    porcentagem = ((frame + 1) / len(xs)) * 100
    texto.set_text(
        f'⏱️ Tempo: {tempo:.2f}s\n'
        f'📊 Progresso: {frame+1}/{len(xs)} ({porcentagem:.1f}%)\n'
        f'📍 X={xs[frame]:6.2f}  Y={ys[frame]:6.2f}  Z={zs[frame]:6.2f}'
    )
    
    # Rotação suave da câmera para melhor visualização
    elevacao = 20 + 10 * np.sin(frame / 100)
    azimute = frame * 0.3
    ax.view_init(elev=elevacao, azim=azimute)
    
    return linha, ponto, texto

print("\n🎬 Iniciando animação...")
print("A trajetória será desenhada completamente SEM APAGAR!")
print("A câmera rotacionará automaticamente para melhor visualização.")
print("Pressione Ctrl+C ou feche a janela para parar\n")

# Criar animação
anim = FuncAnimation(
    fig, 
    update, 
    init_func=init,
    frames=len(xs),
    interval=10,  # 10ms entre frames
    blit=True,
    repeat=True
)

plt.tight_layout()
plt.show()

print("\n✅ Animação encerrada!")
