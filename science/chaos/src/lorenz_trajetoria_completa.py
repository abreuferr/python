"""
Animação do Atrator de Lorenz - Versão com Trajetória Completa
A trajetória NÃO é apagada, crescendo continuamente
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def lorenz(x, y, z, sigma=10, rho=28, beta=8/3):
    """
    Calcula as derivadas do sistema de Lorenz
    
    Parâmetros:
    - x, y, z: coordenadas atuais
    - sigma, rho, beta: parâmetros do sistema (valores clássicos)
    
    Retorna:
    - dx/dt, dy/dt, dz/dt
    """
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

def simular_lorenz(x0=0, y0=1, z0=1.05, dt=0.01, num_passos=10000, 
                   sigma=10, rho=28, beta=8/3):
    """
    Simula o sistema de Lorenz usando o método de Euler
    """
    xs = np.zeros(num_passos)
    ys = np.zeros(num_passos)
    zs = np.zeros(num_passos)
    
    xs[0], ys[0], zs[0] = x0, y0, z0
    
    for i in range(num_passos - 1):
        dx, dy, dz = lorenz(xs[i], ys[i], zs[i], sigma, rho, beta)
        xs[i + 1] = xs[i] + dx * dt
        ys[i + 1] = ys[i] + dy * dt
        zs[i + 1] = zs[i] + dz * dt
    
    return xs, ys, zs

class AnimacaoLorenzCompleta:
    """Animação do Atrator de Lorenz com trajetória completa (sem apagar)"""
    
    def __init__(self, xs, ys, zs, intervalo=20):
        """
        Inicializa a animação
        
        Parâmetros:
        - xs, ys, zs: trajetórias completas
        - intervalo: tempo entre frames em ms
        """
        self.xs = xs
        self.ys = ys
        self.zs = zs
        self.intervalo = intervalo
        
        # Configurar figura
        self.fig = plt.figure(figsize=(14, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Configurar limites dos eixos
        self.ax.set_xlim([xs.min() - 5, xs.max() + 5])
        self.ax.set_ylim([ys.min() - 5, ys.max() + 5])
        self.ax.set_zlim([zs.min() - 5, zs.max() + 5])
        
        # Labels
        self.ax.set_xlabel('X', fontsize=12)
        self.ax.set_ylabel('Y', fontsize=12)
        self.ax.set_zlabel('Z', fontsize=12)
        self.ax.set_title('Atrator de Lorenz - Trajetória Completa', 
                         fontsize=16, fontweight='bold')
        
        # Inicializar linha (trajetória crescente) e ponto
        self.linha, = self.ax.plot([], [], [], 'b-', alpha=0.6, linewidth=1.5)
        self.ponto, = self.ax.plot([], [], [], 'ro', markersize=10)
        
        # Adicionar ponto inicial em verde
        self.ax.scatter([xs[0]], [ys[0]], [zs[0]], color='green', 
                       s=150, marker='o', label='Início', edgecolors='darkgreen', linewidths=2)
        
        # Texto para mostrar informações
        self.texto = self.ax.text2D(0.02, 0.95, '', transform=self.ax.transAxes, 
                                    fontsize=12, verticalalignment='top',
                                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
        
        self.ax.legend(loc='upper right')
        
    def init(self):
        """Inicializa a animação"""
        self.linha.set_data([], [])
        self.linha.set_3d_properties([])
        self.ponto.set_data([], [])
        self.ponto.set_3d_properties([])
        self.texto.set_text('')
        return self.linha, self.ponto, self.texto
    
    def update(self, frame):
        """Atualiza cada frame da animação"""
        # A trajetória cresce do início até o frame atual (NÃO apaga!)
        self.linha.set_data(self.xs[:frame+1], self.ys[:frame+1])
        self.linha.set_3d_properties(self.zs[:frame+1])
        
        # Atualizar ponto (posição atual)
        self.ponto.set_data([self.xs[frame]], [self.ys[frame]])
        self.ponto.set_3d_properties([self.zs[frame]])
        
        # Atualizar texto
        tempo = frame * 0.01
        comprimento = frame + 1
        self.texto.set_text(
            f'Tempo: {tempo:.2f}s\n'
            f'Pontos desenhados: {comprimento}/{len(self.xs)}\n'
            f'Posição: ({self.xs[frame]:.1f}, {self.ys[frame]:.1f}, {self.zs[frame]:.1f})'
        )
        
        return self.linha, self.ponto, self.texto
    
    def animar(self, salvar=False, nome_arquivo='lorenz_completa.gif'):
        """Cria e exibe a animação"""
        anim = FuncAnimation(
            self.fig, 
            self.update, 
            init_func=self.init,
            frames=len(self.xs),
            interval=self.intervalo,
            blit=True,
            repeat=True
        )
        
        if salvar:
            print(f"Salvando animação em '{nome_arquivo}'...")
            anim.save(nome_arquivo, writer='pillow', fps=30, dpi=100)
            print("Animação salva com sucesso!")
        
        plt.show()
        return anim

class AnimacaoLorenzCompletaRotativa:
    """Animação com trajetória completa E câmera rotativa"""
    
    def __init__(self, xs, ys, zs, intervalo=20, rotacao=True):
        """
        Inicializa a animação
        
        Parâmetros:
        - xs, ys, zs: trajetórias completas
        - intervalo: tempo entre frames em ms
        - rotacao: se True, a câmera rotaciona automaticamente
        """
        self.xs = xs
        self.ys = ys
        self.zs = zs
        self.intervalo = intervalo
        self.rotacao = rotacao
        
        # Configurar figura
        self.fig = plt.figure(figsize=(14, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Configurar limites dos eixos
        margem = 5
        self.ax.set_xlim([xs.min() - margem, xs.max() + margem])
        self.ax.set_ylim([ys.min() - margem, ys.max() + margem])
        self.ax.set_zlim([zs.min() - margem, zs.max() + margem])
        
        # Labels
        self.ax.set_xlabel('X', fontsize=12, labelpad=10)
        self.ax.set_ylabel('Y', fontsize=12, labelpad=10)
        self.ax.set_zlabel('Z', fontsize=12, labelpad=10)
        self.ax.set_title('Atrator de Lorenz - Trajetória Crescente com Rotação', 
                         fontsize=16, fontweight='bold', pad=20)
        
        # Inicializar linha (trajetória crescente) e ponto
        self.linha, = self.ax.plot([], [], [], 'b-', alpha=0.7, linewidth=1.5)
        self.ponto, = self.ax.plot([], [], [], 'ro', markersize=12, 
                                   markeredgecolor='darkred', markeredgewidth=2)
        
        # Marcar início
        self.ax.scatter([xs[0]], [ys[0]], [zs[0]], color='lime', 
                       s=200, marker='*', label='Início', 
                       edgecolors='darkgreen', linewidths=2, zorder=5)
        
        # Texto informativo
        self.texto = self.ax.text2D(0.02, 0.98, '', transform=self.ax.transAxes, 
                                    fontsize=11, verticalalignment='top',
                                    bbox=dict(boxstyle='round', facecolor='lightblue', 
                                            alpha=0.8, edgecolor='navy'))
        
        self.ax.legend(loc='upper right', fontsize=10)
        
        # Grade sutil
        self.ax.grid(True, alpha=0.3, linestyle='--')
        
    def init(self):
        """Inicializa a animação"""
        self.linha.set_data([], [])
        self.linha.set_3d_properties([])
        self.ponto.set_data([], [])
        self.ponto.set_3d_properties([])
        self.texto.set_text('')
        return self.linha, self.ponto, self.texto
    
    def update(self, frame):
        """Atualiza cada frame da animação"""
        # A trajetória cresce continuamente
        self.linha.set_data(self.xs[:frame+1], self.ys[:frame+1])
        self.linha.set_3d_properties(self.zs[:frame+1])
        
        # Atualizar ponto atual
        self.ponto.set_data([self.xs[frame]], [self.ys[frame]])
        self.ponto.set_3d_properties([self.zs[frame]])
        
        # Atualizar texto
        tempo = frame * 0.01
        porcentagem = ((frame + 1) / len(self.xs)) * 100
        self.texto.set_text(
            f'⏱️ Tempo: {tempo:.2f}s\n'
            f'📊 Progresso: {frame+1}/{len(self.xs)} ({porcentagem:.1f}%)\n'
            f'📍 Posição atual:\n'
            f'   X = {self.xs[frame]:6.2f}\n'
            f'   Y = {self.ys[frame]:6.2f}\n'
            f'   Z = {self.zs[frame]:6.2f}'
        )
        
        # Rotação suave da câmera
        if self.rotacao:
            elevacao = 20 + 10 * np.sin(frame / 100)
            azimute = frame * 0.3
            self.ax.view_init(elev=elevacao, azim=azimute)
        
        return self.linha, self.ponto, self.texto
    
    def animar(self):
        """Cria e exibe a animação"""
        anim = FuncAnimation(
            self.fig, 
            self.update, 
            init_func=self.init,
            frames=len(self.xs),
            interval=self.intervalo,
            blit=True,
            repeat=True
        )
        
        plt.show()
        return anim

class AnimacaoMultiplasCompleta:
    """Múltiplas trajetórias crescentes simultaneamente"""
    
    def __init__(self, trajetorias, cores=None, intervalo=20, rotacao=True):
        """
        Inicializa animação com múltiplas trajetórias completas
        
        Parâmetros:
        - trajetorias: lista de tuplas (xs, ys, zs)
        - cores: lista de cores para cada trajetória
        - intervalo: tempo entre frames em ms
        - rotacao: se True, câmera rotaciona
        """
        self.trajetorias = trajetorias
        self.num_trajetorias = len(trajetorias)
        self.intervalo = intervalo
        self.rotacao = rotacao
        
        if cores is None:
            cores = ['blue', 'red', 'green', 'orange', 'purple', 'cyan']
        self.cores = cores[:self.num_trajetorias]
        
        # Configurar figura
        self.fig = plt.figure(figsize=(15, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Determinar limites
        all_xs = np.concatenate([t[0] for t in trajetorias])
        all_ys = np.concatenate([t[1] for t in trajetorias])
        all_zs = np.concatenate([t[2] for t in trajetorias])
        
        margem = 5
        self.ax.set_xlim([all_xs.min() - margem, all_xs.max() + margem])
        self.ax.set_ylim([all_ys.min() - margem, all_ys.max() + margem])
        self.ax.set_zlim([all_zs.min() - margem, all_zs.max() + margem])
        
        # Labels
        self.ax.set_xlabel('X', fontsize=12)
        self.ax.set_ylabel('Y', fontsize=12)
        self.ax.set_zlabel('Z', fontsize=12)
        self.ax.set_title('Efeito Borboleta - Trajetórias Completas', 
                         fontsize=16, fontweight='bold')
        
        # Inicializar linhas e pontos
        self.linhas = []
        self.pontos = []
        for i, cor in enumerate(self.cores):
            linha, = self.ax.plot([], [], [], '-', color=cor, alpha=0.7, 
                                 linewidth=1.5, label=f'Trajetória {i+1}')
            ponto, = self.ax.plot([], [], [], 'o', color=cor, markersize=10,
                                 markeredgecolor='black', markeredgewidth=1)
            self.linhas.append(linha)
            self.pontos.append(ponto)
        
        # Marcar pontos iniciais
        for i, (xs, ys, zs) in enumerate(trajetorias):
            self.ax.scatter([xs[0]], [ys[0]], [zs[0]], 
                          color=self.cores[i], s=150, marker='*',
                          edgecolors='black', linewidths=2, zorder=5)
        
        self.ax.legend(loc='upper right', fontsize=9)
        self.ax.grid(True, alpha=0.3)
        
        # Texto
        self.texto = self.ax.text2D(0.02, 0.95, '', transform=self.ax.transAxes, 
                                    fontsize=11, verticalalignment='top',
                                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
    def init(self):
        """Inicializa animação"""
        for linha, ponto in zip(self.linhas, self.pontos):
            linha.set_data([], [])
            linha.set_3d_properties([])
            ponto.set_data([], [])
            ponto.set_3d_properties([])
        self.texto.set_text('')
        return self.linhas + self.pontos + [self.texto]
    
    def update(self, frame):
        """Atualiza cada frame"""
        # Atualizar cada trajetória (crescente)
        for i, (xs, ys, zs) in enumerate(self.trajetorias):
            self.linhas[i].set_data(xs[:frame+1], ys[:frame+1])
            self.linhas[i].set_3d_properties(zs[:frame+1])
            
            self.pontos[i].set_data([xs[frame]], [ys[frame]])
            self.pontos[i].set_3d_properties([zs[frame]])
        
        # Calcular distância entre primeira e segunda trajetória
        xs1, ys1, zs1 = self.trajetorias[0]
        xs2, ys2, zs2 = self.trajetorias[1]
        distancia = np.sqrt((xs1[frame] - xs2[frame])**2 + 
                           (ys1[frame] - ys2[frame])**2 + 
                           (zs1[frame] - zs2[frame])**2)
        
        # Texto
        tempo = frame * 0.01
        self.texto.set_text(
            f'⏱️ Tempo: {tempo:.2f}s\n'
            f'📏 Distância entre traj. 1 e 2: {distancia:.2f}\n'
            f'📊 Frame: {frame+1}'
        )
        
        # Rotação
        if self.rotacao:
            self.ax.view_init(elev=20, azim=frame * 0.3)
        
        return self.linhas + self.pontos + [self.texto]
    
    def animar(self):
        """Cria e exibe animação"""
        num_frames = min([len(t[0]) for t in self.trajetorias])
        
        anim = FuncAnimation(
            self.fig, 
            self.update, 
            init_func=self.init,
            frames=num_frames,
            interval=self.intervalo,
            blit=True,
            repeat=True
        )
        
        plt.show()
        return anim

def menu():
    """Menu interativo"""
    print("=" * 70)
    print("ANIMAÇÃO DO ATRATOR DE LORENZ - TRAJETÓRIA COMPLETA (SEM APAGAR)")
    print("=" * 70)
    print("\nEscolha o tipo de animação:")
    print("1 - Trajetória completa crescente (vista estática)")
    print("2 - Trajetória completa crescente com câmera rotativa")
    print("3 - Múltiplas trajetórias crescentes (efeito borboleta)")
    print("0 - Sair")
    print("=" * 70)
    
    escolha = input("\nSua escolha: ")
    return escolha

if __name__ == "__main__":
    escolha = menu()
    
    if escolha == '1':
        print("\n✨ Gerando trajetória...")
        xs, ys, zs = simular_lorenz(num_passos=5000)
        print(f"✓ {len(xs)} pontos gerados")
        
        print("\n🎬 Iniciando animação...")
        print("A trajetória será desenhada completamente, sem apagar!")
        print("Feche a janela para encerrar.\n")
        
        animacao = AnimacaoLorenzCompleta(xs, ys, zs, intervalo=10)
        animacao.animar()
        
    elif escolha == '2':
        print("\n✨ Gerando trajetória...")
        xs, ys, zs = simular_lorenz(num_passos=5000)
        print(f"✓ {len(xs)} pontos gerados")
        
        print("\n🎬 Iniciando animação com câmera rotativa...")
        print("A trajetória cresce E a câmera rotaciona!")
        print("Feche a janela para encerrar.\n")
        
        animacao = AnimacaoLorenzCompletaRotativa(xs, ys, zs, intervalo=10, rotacao=True)
        animacao.animar()
        
    elif escolha == '3':
        print("\n✨ Gerando múltiplas trajetórias...")
        
        condicoes_iniciais = [
            (0, 1, 1.05),
            (0.01, 1, 1.05),
            (0, 1.01, 1.05),
            (0, 1, 1.0501)
        ]
        
        trajetorias = []
        for x0, y0, z0 in condicoes_iniciais:
            xs, ys, zs = simular_lorenz(x0=x0, y0=y0, z0=z0, num_passos=4000)
            trajetorias.append((xs, ys, zs))
            print(f"  ✓ Trajetória: x0={x0}, y0={y0}, z0={z0}")
        
        print(f"\n✓ {len(trajetorias)} trajetórias geradas")
        print("\n🎬 Iniciando animação...")
        print("Observe as trajetórias crescerem e divergirem!")
        print("Feche a janela para encerrar.\n")
        
        animacao = AnimacaoMultiplasCompleta(trajetorias, intervalo=10, rotacao=True)
        animacao.animar()
        
    elif escolha == '0':
        print("\n👋 Encerrando...")
    else:
        print("\n❌ Opção inválida!")
