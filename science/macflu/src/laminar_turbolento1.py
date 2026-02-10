import numpy as np
import matplotlib.pyplot as plt

def plot_flow_profiles():
    r = np.linspace(-1, 1, 100)  # Raio do cano (de -1 a 1)
    
    # Perfil Laminar: v(r) = Vmax * (1 - r^2)
    v_laminar = 1 - r**2
    
    # Perfil Turbulento (Lei da Potência de 1/7): v(r) = Vmax * (1 - |r|)^(1/7)
    v_turbulent = (1 - np.abs(r))**(1/7)

    plt.figure(figsize=(10, 6))
    
    # Desenhando os perfis
    plt.plot(v_laminar, r, label='Laminar (Suave/Parabólico)', lw=3, color='blue')
    plt.plot(v_turbulent, r, label='Turbulento (Caótico/Achatado)', lw=3, color='red', linestyle='--')

    # Estilização do gráfico
    plt.title('Comparação de Perfis de Velocidade em um Cano', fontsize=14)
    plt.xlabel('Velocidade Relativa')
    plt.ylabel('Posição no Cano (Raio)')
    plt.axhline(0, color='black', lw=1)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    print("Exibindo o gráfico... O perfil azul mostra camadas organizadas.")
    print("O perfil vermelho mostra como a turbulência uniformiza a velocidade no centro.")
    plt.show()

if __name__ == "__main__":
    plot_flow_profiles()