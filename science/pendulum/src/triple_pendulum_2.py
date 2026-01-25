import time
import os
import math

class TriplePendulum:
    def __init__(self, L1=1.0, L2=1.0, L3=1.0, m1=1.0, m2=1.0, m3=1.0):
        # Comprimentos
        self.L1, self.L2, self.L3 = L1, L2, L3
        # Massas
        self.m1, self.m2, self.m3 = m1, m2, m3
        # Gravidade
        self.g = 9.81
        
        # Estado inicial [theta1, theta2, theta3, omega1, omega2, omega3]
        self.state = [math.pi/2, math.pi/2, math.pi/2, 0.0, 0.0, 0.0]
        
    def derivatives(self, state):
        """Calcula as derivadas do sistema"""
        th1, th2, th3, w1, w2, w3 = state
        
        # Fatores comuns
        c12 = math.cos(th1 - th2)
        c23 = math.cos(th2 - th3)
        c13 = math.cos(th1 - th3)
        s12 = math.sin(th1 - th2)
        s23 = math.sin(th2 - th3)
        s13 = math.sin(th1 - th3)
        
        # Sistema simplificado de equações
        M = self.m1 + self.m2 + self.m3
        
        # Acelerações angulares (aproximação simplificada)
        den1 = self.L1 * (M - self.m2 * c12**2 - self.m3 * c13**2)
        den2 = self.L2 * (self.m2 + self.m3 - self.m3 * c23**2)
        den3 = self.L3 * self.m3
        
        num1 = -M * self.g * math.sin(th1) - self.m2 * self.L2 * w2**2 * s12 - self.m3 * self.L3 * w3**2 * s13
        num2 = -(self.m2 + self.m3) * self.g * math.sin(th2) + self.m2 * self.L1 * w1**2 * s12 - self.m3 * self.L3 * w3**2 * s23
        num3 = -self.m3 * self.g * math.sin(th3) + self.m3 * self.L2 * w2**2 * s23 + self.m3 * self.L1 * w1**2 * s13
        
        alpha1 = num1 / den1 if abs(den1) > 1e-10 else 0
        alpha2 = num2 / den2 if abs(den2) > 1e-10 else 0
        alpha3 = num3 / den3 if abs(den3) > 1e-10 else 0
        
        return [w1, w2, w3, alpha1, alpha2, alpha3]
    
    def step(self, dt):
        """Integração usando método de Runge-Kutta de 4ª ordem"""
        # k1
        k1 = self.derivatives(self.state)
        k1 = [k * dt for k in k1]
        
        # k2
        state2 = [self.state[i] + k1[i]/2 for i in range(6)]
        k2 = self.derivatives(state2)
        k2 = [k * dt for k in k2]
        
        # k3
        state3 = [self.state[i] + k2[i]/2 for i in range(6)]
        k3 = self.derivatives(state3)
        k3 = [k * dt for k in k3]
        
        # k4
        state4 = [self.state[i] + k3[i] for i in range(6)]
        k4 = self.derivatives(state4)
        k4 = [k * dt for k in k4]
        
        # Atualizar estado
        for i in range(6):
            self.state[i] += (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6
        
    def get_positions(self):
        """Retorna as posições (x, y) de cada massa"""
        th1, th2, th3 = self.state[0:3]
        
        x1 = self.L1 * math.sin(th1)
        y1 = -self.L1 * math.cos(th1)
        
        x2 = x1 + self.L2 * math.sin(th2)
        y2 = y1 - self.L2 * math.cos(th2)
        
        x3 = x2 + self.L3 * math.sin(th3)
        y3 = y2 - self.L3 * math.cos(th3)
        
        return [(0, 0), (x1, y1), (x2, y2), (x3, y3)]

def draw_pendulum(positions, width=80, height=24):
    """Desenha o pêndulo no terminal"""
    # Criar grid
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Escala para caber na tela
    scale = min(width, height) / 7
    offset_x = width // 2
    offset_y = 5
    
    # Converter posições para coordenadas da tela
    screen_pos = []
    for x, y in positions:
        sx = int(offset_x + x * scale)
        sy = int(offset_y - y * scale)
        sx = max(0, min(width-1, sx))
        sy = max(0, min(height-1, sy))
        screen_pos.append((sx, sy))
    
    # Desenhar linhas
    for i in range(len(screen_pos) - 1):
        x0, y0 = screen_pos[i]
        x1, y1 = screen_pos[i+1]
        
        # Linha simples
        steps = max(abs(x1-x0), abs(y1-y0))
        if steps > 0:
            for step in range(steps + 1):
                t = step / steps
                x = int(x0 + t * (x1 - x0))
                y = int(y0 + t * (y1 - y0))
                if 0 <= x < width and 0 <= y < height:
                    grid[y][x] = '│' if abs(x1-x0) < abs(y1-y0) else '─'
    
    # Desenhar massas
    symbols = ['◉', '●', '●', '◉']
    for i, (x, y) in enumerate(screen_pos):
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = symbols[i]
    
    return '\n'.join([''.join(row) for row in grid])

def main():
    print("=== SIMULAÇÃO DE PÊNDULO TRIPLO ===")
    print("Pressione Ctrl+C para sair\n")
    time.sleep(1)
    
    # Criar pêndulo
    pendulum = TriplePendulum(L1=1.0, L2=1.0, L3=1.0)
    
    # Parâmetros de simulação
    dt = 0.02
    frame_delay = 0.05
    
    try:
        t = 0
        while True:
            # Limpar terminal
            os.system('clear' if os.name != 'nt' else 'cls')
            
            # Atualizar física
            pendulum.step(dt)
            
            # Obter posições
            positions = pendulum.get_positions()
            
            # Desenhar
            frame = draw_pendulum(positions)
            print(frame)
            
            # Informações
            th1, th2, th3 = pendulum.state[0:3]
            print(f"\nTempo: {t:.2f}s")
            print(f"Ângulos: θ1={math.degrees(th1):.1f}° θ2={math.degrees(th2):.1f}° θ3={math.degrees(th3):.1f}°")
            
            # Energia (aproximada)
            E = pendulum.m1 * pendulum.g * (-pendulum.L1 * math.cos(th1))
            E += pendulum.m2 * pendulum.g * (-pendulum.L1 * math.cos(th1) - pendulum.L2 * math.cos(th2))
            E += pendulum.m3 * pendulum.g * (-pendulum.L1 * math.cos(th1) - pendulum.L2 * math.cos(th2) - pendulum.L3 * math.cos(th3))
            print(f"Energia potencial: {E:.2f} J")
            
            time.sleep(frame_delay)
            t += dt
            
    except KeyboardInterrupt:
        print("\n\nSimulação encerrada!")

if __name__ == "__main__":
    main()