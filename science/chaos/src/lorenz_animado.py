"""
Animação do Atrator de Lorenz
Sistema caótico clássico com visualização animada em tempo real
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib import cm

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
    
    Parâmetros:
    - x0, y0, z0: condições iniciais
    - dt: passo de tempo
    - num_passos: número de iterações
    - sigma, rho, beta: parâmetros do sistema
    
    Retorna:
    - Arrays com as trajetórias x, y, z
    """
    # Arrays para armazenar a trajetória
    xs = np.zeros(num_passos)
    ys = np.zeros(num_passos)
    zs = np.zeros(num_passos)
    
    # Condições iniciais
    xs[0], ys[0], zs[0] = x0, y0, z0
    
    # Integração numérica (método de Euler)
    for i in range(num_passos - 1):
        dx, dy, dz = lorenz(xs[i], ys[i], zs[i], sigma, rho, beta)
        xs[i + 1] = xs[i] + dx * dt
        ys[i + 1] = ys[i] + dy * dt
        zs[i + 1] = zs[i] + dz * dt
    
    return xs, ys, zs

class AnimacaoLorenz:
    """Classe para criar animação do Atrator de Lorenz"""
    
    def __init__(self, xs, ys, zs, intervalo=20, tamanho_cauda=100):
        """
        Inicializa a animação
        
        Parâmetros:
        - xs, ys, zs: trajetórias completas
        - intervalo: tempo entre frames em ms
        - tamanho_cauda: número de pontos da cauda visível
        """
        self.xs = xs
        self.ys = ys
        self.zs = zs
        self.intervalo = intervalo
        self.tamanho_cauda = tamanho_cauda
        self.frame_atual = 0
        
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
        self.ax.set_title('Atrator de Lorenz - Animação', fontsize=16, fontweight='bold')
        
        # Inicializar linha e ponto
        self.linha, = self.ax.plot([], [], [], 'b-', alpha=0.6, linewidth=1.5)
        self.ponto, = self.ax.plot([], [], [], 'ro', markersize=10)
        
        # Texto para mostrar o frame atual
        self.texto = self.ax.text2D(0.02, 0.95, '', transform=self.ax.transAxes, 
                                    fontsize=12, verticalalignment='top')
        
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
        # Determinar intervalo de pontos para mostrar (cauda)
        inicio = max(0, frame - self.tamanho_cauda)
        fim = frame + 1
        
        # Atualizar linha (cauda)
        self.linha.set_data(self.xs[inicio:fim], self.ys[inicio:fim])
        self.linha.set_3d_properties(self.zs[inicio:fim])
        
        # Atualizar ponto (posição atual)
        self.ponto.set_data([self.xs[frame]], [self.ys[frame]])
        self.ponto.set_3d_properties([self.zs[frame]])
        
        # Atualizar texto
        tempo = frame * 0.01
        self.texto.set_text(f'Tempo: {tempo:.2f}s\nFrame: {frame}/{len(self.xs)}')
        
        # Rotacionar vista gradualmente
        self.ax.view_init(elev=20, azim=frame * 0.3)
        
        return self.linha, self.ponto, self.texto
    
    def animar(self, salvar=False, nome_arquivo='lorenz_animacao.gif'):
        """
        Cria e exibe a animação
        
        Parâmetros:
        - salvar: se True, salva a animação como GIF
        - nome_arquivo: nome do arquivo para salvar
        """
        # Criar animação (usar apenas parte dos dados para velocidade)
        num_frames = min(2000, len(self.xs))
        
        anim = FuncAnimation(
            self.fig, 
            self.update, 
            init_func=self.init,
            frames=num_frames,
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

class AnimacaoMultipla:
    """Animação com múltiplas trajetórias (efeito borboleta)"""
    
    def __init__(self, trajetorias, cores=None, intervalo=20, tamanho_cauda=100):
        """
        Inicializa animação com múltiplas trajetórias
        
        Parâmetros:
        - trajetorias: lista de tuplas (xs, ys, zs)
        - cores: lista de cores para cada trajetória
        - intervalo: tempo entre frames em ms
        - tamanho_cauda: número de pontos da cauda visível
        """
        self.trajetorias = trajetorias
        self.num_trajetorias = len(trajetorias)
        self.intervalo = intervalo
        self.tamanho_cauda = tamanho_cauda
        
        if cores is None:
            cores = ['blue', 'red', 'green', 'orange', 'purple', 'cyan']
        self.cores = cores[:self.num_trajetorias]
        
        # Configurar figura
        self.fig = plt.figure(figsize=(14, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Determinar limites dos eixos
        all_xs = np.concatenate([t[0] for t in trajetorias])
        all_ys = np.concatenate([t[1] for t in trajetorias])
        all_zs = np.concatenate([t[2] for t in trajetorias])
        
        self.ax.set_xlim([all_xs.min() - 5, all_xs.max() + 5])
        self.ax.set_ylim([all_ys.min() - 5, all_ys.max() + 5])
        self.ax.set_zlim([all_zs.min() - 5, all_zs.max() + 5])
        
        # Labels
        self.ax.set_xlabel('X', fontsize=12)
        self.ax.set_ylabel('Y', fontsize=12)
        self.ax.set_zlabel('Z', fontsize=12)
        self.ax.set_title('Atrator de Lorenz - Sensibilidade às Condições Iniciais', 
                         fontsize=14, fontweight='bold')
        
        # Inicializar linhas e pontos para cada trajetória
        self.linhas = []
        self.pontos = []
        for cor in self.cores:
            linha, = self.ax.plot([], [], [], '-', color=cor, alpha=0.6, linewidth=1.5)
            ponto, = self.ax.plot([], [], [], 'o', color=cor, markersize=8)
            self.linhas.append(linha)
            self.pontos.append(ponto)
        
        # Texto
        self.texto = self.ax.text2D(0.02, 0.95, '', transform=self.ax.transAxes, 
                                    fontsize=12, verticalalignment='top')
        
    def init(self):
        """Inicializa a animação"""
        for linha, ponto in zip(self.linhas, self.pontos):
            linha.set_data([], [])
            linha.set_3d_properties([])
            ponto.set_data([], [])
            ponto.set_3d_properties([])
        self.texto.set_text('')
        return self.linhas + self.pontos + [self.texto]
    
    def update(self, frame):
        """Atualiza cada frame da animação"""
        # Atualizar cada trajetória
        for i, (xs, ys, zs) in enumerate(self.trajetorias):
            inicio = max(0, frame - self.tamanho_cauda)
            fim = frame + 1
            
            # Atualizar linha
            self.linhas[i].set_data(xs[inicio:fim], ys[inicio:fim])
            self.linhas[i].set_3d_properties(zs[inicio:fim])
            
            # Atualizar ponto
            self.pontos[i].set_data([xs[frame]], [ys[frame]])
            self.pontos[i].set_3d_properties([zs[frame]])
        
        # Atualizar texto
        tempo = frame * 0.01
        self.texto.set_text(f'Tempo: {tempo:.2f}s\nFrame: {frame}')
        
        # Rotacionar vista gradualmente
        self.ax.view_init(elev=20, azim=frame * 0.3)
        
        return self.linhas + self.pontos + [self.texto]
    
    def animar(self):
        """Cria e exibe a animação"""
        # Determinar número de frames (usar o mínimo entre todas as trajetórias)
        num_frames = min([len(t[0]) for t in self.trajetorias])
        num_frames = min(2000, num_frames)
        
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
    """Menu interativo para escolher tipo de animação"""
    print("=" * 60)
    print("SIMULAÇÃO ANIMADA DO ATRATOR DE LORENZ")
    print("=" * 60)
    print("\nEscolha o tipo de animação:")
    print("1 - Animação simples (uma trajetória)")
    print("2 - Múltiplas trajetórias (efeito borboleta)")
    print("3 - Salvar animação como GIF")
    print("0 - Sair")
    print("=" * 60)
    
    escolha = input("\nSua escolha: ")
    return escolha

if __name__ == "__main__":
    escolha = menu()
    
    if escolha == '1':
        print("\nGerando trajetória...")
        xs, ys, zs = simular_lorenz(num_passos=5000)
        print(f"Trajetória gerada com {len(xs)} pontos")
        
        print("\nIniciando animação...")
        print("Feche a janela para encerrar.")
        animacao = AnimacaoLorenz(xs, ys, zs, intervalo=20, tamanho_cauda=150)
        animacao.animar()
        
    elif escolha == '2':
        print("\nGerando múltiplas trajetórias com condições iniciais próximas...")
        
        # Gerar 4 trajetórias com pequenas variações
        condicoes_iniciais = [
            (0, 1, 1.05),
            (0.01, 1, 1.05),
            (0, 1.01, 1.05),
            (0, 1, 1.0501)
        ]
        
        trajetorias = []
        for x0, y0, z0 in condicoes_iniciais:
            xs, ys, zs = simular_lorenz(x0=x0, y0=y0, z0=z0, num_passos=5000)
            trajetorias.append((xs, ys, zs))
            print(f"  Trajetória gerada: x0={x0}, y0={y0}, z0={z0}")
        
        print("\nIniciando animação...")
        print("Observe como trajetórias inicialmente próximas divergem!")
        print("Feche a janela para encerrar.")
        animacao = AnimacaoMultipla(trajetorias, intervalo=20, tamanho_cauda=150)
        animacao.animar()
        
    elif escolha == '3':
        print("\nGerando trajetória...")
        xs, ys, zs = simular_lorenz(num_passos=3000)
        print(f"Trajetória gerada com {len(xs)} pontos")
        
        nome_arquivo = input("\nNome do arquivo (default: lorenz_animacao.gif): ").strip()
        if not nome_arquivo:
            nome_arquivo = "lorenz_animacao.gif"
        if not nome_arquivo.endswith('.gif'):
            nome_arquivo += '.gif'
        
        print("\nCriando animação...")
        print("Isso pode levar alguns minutos...")
        animacao = AnimacaoLorenz(xs, ys, zs, intervalo=50, tamanho_cauda=100)
        animacao.animar(salvar=True, nome_arquivo=nome_arquivo)
        
    elif escolha == '0':
        print("\nEncerrando...")
    else:
        print("\nOpção inválida!")
