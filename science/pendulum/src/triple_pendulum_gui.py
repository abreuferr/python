import tkinter as tk
from tkinter import ttk
import math

class TriplePendulum:
    def __init__(self, L1=1.0, L2=1.0, L3=1.0, m1=1.0, m2=1.0, m3=1.0):
        self.L1, self.L2, self.L3 = L1, L2, L3
        self.m1, self.m2, self.m3 = m1, m2, m3
        self.g = 9.81
        self.state = [math.pi/2, math.pi/2, math.pi/2, 0.0, 0.0, 0.0]
        self.trail = []
        
    def derivatives(self, state):
        th1, th2, th3, w1, w2, w3 = state
        
        c12 = math.cos(th1 - th2)
        c23 = math.cos(th2 - th3)
        c13 = math.cos(th1 - th3)
        s12 = math.sin(th1 - th2)
        s23 = math.sin(th2 - th3)
        s13 = math.sin(th1 - th3)
        
        M = self.m1 + self.m2 + self.m3
        
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
        k1 = self.derivatives(self.state)
        k1 = [k * dt for k in k1]
        
        state2 = [self.state[i] + k1[i]/2 for i in range(6)]
        k2 = self.derivatives(state2)
        k2 = [k * dt for k in k2]
        
        state3 = [self.state[i] + k2[i]/2 for i in range(6)]
        k3 = self.derivatives(state3)
        k3 = [k * dt for k in k3]
        
        state4 = [self.state[i] + k3[i] for i in range(6)]
        k4 = self.derivatives(state4)
        k4 = [k * dt for k in k4]
        
        for i in range(6):
            self.state[i] += (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6
        
    def get_positions(self):
        th1, th2, th3 = self.state[0:3]
        
        x1 = self.L1 * math.sin(th1)
        y1 = self.L1 * math.cos(th1)
        
        x2 = x1 + self.L2 * math.sin(th2)
        y2 = y1 + self.L2 * math.cos(th2)
        
        x3 = x2 + self.L3 * math.sin(th3)
        y3 = y2 + self.L3 * math.cos(th3)
        
        return [(0, 0), (x1, y1), (x2, y2), (x3, y3)]
    
    def reset(self, th1, th2, th3):
        self.state = [th1, th2, th3, 0.0, 0.0, 0.0]
        self.trail = []

class PendulumGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulação de Pêndulo Triplo")
        self.root.geometry("900x700")
        self.root.configure(bg='#1e1e1e')
        
        # Pendulum
        self.pendulum = TriplePendulum(L1=100, L2=100, L3=100)
        self.running = False
        self.show_trail = True
        self.time = 0
        self.dt = 0.015
        self.steps_per_frame = 2  # Múltiplos passos por frame
        
        # Canvas
        canvas_frame = tk.Frame(root, bg='#1e1e1e')
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.canvas = tk.Canvas(canvas_frame, bg='#0a0a0a', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Pré-criar objetos do canvas para melhor performance
        self.trail_lines = []
        self.rod_lines = [self.canvas.create_line(0, 0, 0, 0, width=3) for _ in range(3)]
        self.masses = [self.canvas.create_oval(0, 0, 0, 0) for _ in range(4)]
        
        # Control panel
        control_frame = tk.Frame(root, bg='#2d2d2d', relief=tk.RAISED, bd=2)
        control_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Buttons
        btn_frame = tk.Frame(control_frame, bg='#2d2d2d')
        btn_frame.pack(pady=10)
        
        self.btn_start = tk.Button(btn_frame, text="▶ Iniciar", command=self.toggle_simulation,
                                   bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'),
                                   padx=20, pady=5, relief=tk.FLAT, cursor='hand2')
        self.btn_start.pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="↻ Reiniciar", command=self.reset_simulation,
                 bg='#2196F3', fg='white', font=('Arial', 10, 'bold'),
                 padx=20, pady=5, relief=tk.FLAT, cursor='hand2').pack(side=tk.LEFT, padx=5)
        
        self.btn_trail = tk.Button(btn_frame, text="✓ Rastro", command=self.toggle_trail,
                                   bg='#FF9800', fg='white', font=('Arial', 10, 'bold'),
                                   padx=20, pady=5, relief=tk.FLAT, cursor='hand2')
        self.btn_trail.pack(side=tk.LEFT, padx=5)
        
        # Speed control
        speed_frame = tk.Frame(control_frame, bg='#2d2d2d')
        speed_frame.pack(pady=5)
        
        tk.Label(speed_frame, text="Velocidade:", bg='#2d2d2d', fg='#ffffff',
                font=('Arial', 9)).pack(side=tk.LEFT, padx=5)
        
        self.speed_var = tk.IntVar(value=2)
        for i, label in enumerate(['0.5x', '1x', '2x', '4x']):
            tk.Radiobutton(speed_frame, text=label, variable=self.speed_var, value=i,
                          bg='#2d2d2d', fg='#ffffff', selectcolor='#4CAF50',
                          activebackground='#2d2d2d', activeforeground='#ffffff',
                          command=self.update_speed).pack(side=tk.LEFT, padx=3)
        
        # Sliders
        slider_frame = tk.Frame(control_frame, bg='#2d2d2d')
        slider_frame.pack(pady=10)
        
        self.sliders = []
        self.labels = []
        for i, label in enumerate(["Ângulo θ1:", "Ângulo θ2:", "Ângulo θ3:"]):
            self.create_slider(slider_frame, label, 0, 180, 90, i)
        
        # Info label
        self.info_label = tk.Label(control_frame, text="", bg='#2d2d2d', fg='#ffffff',
                                   font=('Courier', 10))
        self.info_label.pack(pady=5)
        
        self.update()
        
    def create_slider(self, parent, label, from_, to, initial, row):
        frame = tk.Frame(parent, bg='#2d2d2d')
        frame.pack(fill=tk.X, padx=20, pady=2)
        
        tk.Label(frame, text=label, bg='#2d2d2d', fg='#ffffff',
                font=('Arial', 9), width=12, anchor='w').pack(side=tk.LEFT)
        
        slider = ttk.Scale(frame, from_=from_, to=to, orient=tk.HORIZONTAL,
                          command=lambda v: self.update_angle(row, float(v)))
        slider.set(initial)
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        value_label = tk.Label(frame, text=f"{initial}°", bg='#2d2d2d', fg='#00ff00',
                              font=('Courier', 9, 'bold'), width=6)
        value_label.pack(side=tk.LEFT)
        
        self.sliders.append(slider)
        self.labels.append(value_label)
    
    def update_speed(self):
        speeds = [1, 2, 4, 8]
        self.steps_per_frame = speeds[self.speed_var.get()]
    
    def update_angle(self, index, value):
        if not self.running:
            angles = [math.radians(self.sliders[i].get()) for i in range(3)]
            angles[index] = math.radians(value)
            self.pendulum.reset(angles[0], angles[1], angles[2])
        
        self.labels[index].config(text=f"{int(value)}°")
    
    def toggle_simulation(self):
        self.running = not self.running
        if self.running:
            self.btn_start.config(text="⏸ Pausar", bg='#f44336')
        else:
            self.btn_start.config(text="▶ Iniciar", bg='#4CAF50')
    
    def reset_simulation(self):
        self.running = False
        self.time = 0
        self.btn_start.config(text="▶ Iniciar", bg='#4CAF50')
        angles = [math.radians(self.sliders[i].get()) for i in range(3)]
        self.pendulum.reset(angles[0], angles[1], angles[2])
        # Limpar rastro visual
        for line in self.trail_lines:
            self.canvas.delete(line)
        self.trail_lines = []
    
    def toggle_trail(self):
        self.show_trail = not self.show_trail
        if not self.show_trail:
            self.pendulum.trail = []
            for line in self.trail_lines:
                self.canvas.delete(line)
            self.trail_lines = []
            self.btn_trail.config(text="✗ Rastro", bg='#757575')
        else:
            self.btn_trail.config(text="✓ Rastro", bg='#FF9800')
    
    def update(self):
        if self.running:
            # Múltiplos passos de física por frame
            for _ in range(self.steps_per_frame):
                self.pendulum.step(self.dt)
                self.time += self.dt
        
        self.draw()
        self.root.after(16, self.update)  # ~60 FPS
    
    def draw(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_x = width // 2
        center_y = height // 4
        
        positions = self.pendulum.get_positions()
        screen_pos = [(center_x + x, center_y + y) for x, y in positions]
        
        # Trail - otimizado
        if self.show_trail and self.running:
            max_trail = 300
            if len(self.pendulum.trail) > max_trail:
                self.pendulum.trail.pop(0)
                if self.trail_lines:
                    self.canvas.delete(self.trail_lines.pop(0))
            
            if len(self.pendulum.trail) > 0:
                prev = self.pendulum.trail[-1] if self.pendulum.trail else screen_pos[3]
                line = self.canvas.create_line(prev[0], prev[1],
                                              screen_pos[3][0], screen_pos[3][1],
                                              fill='#ff00ff', width=2)
                self.trail_lines.append(line)
            
            self.pendulum.trail.append(screen_pos[3])
        
        # Rods - reutilizar objetos
        colors = ['#00ff00', '#00aaff', '#ff00ff']
        for i in range(3):
            self.canvas.coords(self.rod_lines[i],
                             screen_pos[i][0], screen_pos[i][1],
                             screen_pos[i+1][0], screen_pos[i+1][1])
            self.canvas.itemconfig(self.rod_lines[i], fill=colors[i])
        
        # Masses - reutilizar objetos
        self.canvas.coords(self.masses[0],
                          screen_pos[0][0]-8, screen_pos[0][1]-8,
                          screen_pos[0][0]+8, screen_pos[0][1]+8)
        self.canvas.itemconfig(self.masses[0], fill='#ffffff', outline='#666666', width=2)
        
        for i in range(1, 4):
            r = 12 if i == 3 else 10
            self.canvas.coords(self.masses[i],
                             screen_pos[i][0]-r, screen_pos[i][1]-r,
                             screen_pos[i][0]+r, screen_pos[i][1]+r)
            self.canvas.itemconfig(self.masses[i], fill=colors[i-1], outline='#ffffff', width=2)
        
        # Info - atualizar menos frequentemente
        if int(self.time * 20) % 5 == 0:
            th1, th2, th3 = self.pendulum.state[0:3]
            info = f"Tempo: {self.time:.2f}s  |  θ1: {math.degrees(th1):.1f}°  θ2: {math.degrees(th2):.1f}°  θ3: {math.degrees(th3):.1f}°"
            self.info_label.config(text=info)

def main():
    root = tk.Tk()
    app = PendulumGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()