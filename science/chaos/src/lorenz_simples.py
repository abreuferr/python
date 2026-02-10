"""
Exemplo de execução rápida - Animação do Atrator de Lorenz
Execute este arquivo para ver imediatamente a animação
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
print("Gerando trajetória do Atrator de Lorenz...")
xs, ys, zs = simular_lorenz(num_passos=3000)
print(f"✓ {len(xs)} pontos gerados")

# Configurar animação
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([xs.min() - 5, xs.max() + 5])
ax.set_ylim([ys.min() - 5, ys.max() + 5])
ax.set_zlim([zs.min() - 5, zs.max() + 5])
ax.set_xlabel('X', fontsize=11)
ax.set_ylabel('Y', fontsize=11)
ax.set_zlabel('Z', fontsize=11)
ax.set_title('Atrator de Lorenz - Animação em Tempo Real', fontsize=14, fontweight='bold')

# Elementos da animação
linha, = ax.plot([], [], [], 'b-', alpha=0.7, linewidth=2)
ponto, = ax.plot([], [], [], 'ro', markersize=10)
cauda_tamanho = 100

# Texto informativo
texto = ax.text2D(0.02, 0.95, '', transform=ax.transAxes, 
                  fontsize=11, verticalalignment='top',
                  bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

def init():
    """Inicializa animação"""
    linha.set_data([], [])
    linha.set_3d_properties([])
    ponto.set_data([], [])
    ponto.set_3d_properties([])
    return linha, ponto, texto

def update(frame):
    """Atualiza frame da animação"""
    # Cauda da trajetória
    inicio = max(0, frame - cauda_tamanho)
    fim = frame + 1
    
    linha.set_data(xs[inicio:fim], ys[inicio:fim])
    linha.set_3d_properties(zs[inicio:fim])
    
    # Ponto atual
    ponto.set_data([xs[frame]], [ys[frame]])
    ponto.set_3d_properties([zs[frame]])
    
    # Info
    tempo = frame * 0.01
    texto.set_text(f'Tempo: {tempo:.2f}s\nPonto: ({xs[frame]:.1f}, {ys[frame]:.1f}, {zs[frame]:.1f})')
    
    # Rotação suave da câmera
    ax.view_init(elev=20 + 10*np.sin(frame/100), azim=frame * 0.4)
    
    return linha, ponto, texto

print("\nIniciando animação...")
print("Aperte Ctrl+C ou feche a janela para parar\n")

# Criar animação
anim = FuncAnimation(
    fig, 
    update, 
    init_func=init,
    frames=len(xs),
    interval=20,  # 20ms entre frames = ~50 FPS
    blit=True,
    repeat=True
)

plt.tight_layout()
plt.show()

print("\nAnimação encerrada!")
