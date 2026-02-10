# Animação do Atrator de Lorenz

Simulação animada do famoso Atrator de Lorenz, um sistema dinâmico caótico descoberto por Edward Lorenz em 1963.

## 📋 Descrição

O Atrator de Lorenz é um conjunto de equações diferenciais que descreve o comportamento caótico de sistemas atmosféricos. Este projeto oferece visualizações animadas interativas do atrator.

### Equações do Sistema

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

Parâmetros clássicos: σ = 10, ρ = 28, β = 8/3

## 🚀 Arquivos Disponíveis

### 📂 VERSÕES COM CAUDA (trajetória parcial)

#### 1. `lorenz_simples.py` ⚡
- Execução direta e rápida
- Mostra apenas a "cauda" recente da trajetória
- Câmera rotacionando automaticamente
- Ideal para visualização dinâmica

**Uso:**
```bash
python lorenz_simples.py
```

#### 2. `lorenz_animado.py` 🎮
- Menu interativo com opções
- Animação com cauda ou múltiplas trajetórias
- Demonstra o "efeito borboleta"
- Pode salvar como GIF

**Uso:**
```bash
python lorenz_animado.py
```

**Opções do menu:**
1. Animação simples (uma trajetória com cauda)
2. Múltiplas trajetórias (efeito borboleta)
3. Salvar animação como GIF
0. Sair

---

### 📂 VERSÕES COM TRAJETÓRIA COMPLETA (sem apagar)

#### 3. `lorenz_completo_rapido.py` ⭐ **NOVO!** (RECOMENDADO)
- **A trajetória NÃO é apagada!**
- Desenha o caminho completo do início ao fim
- Câmera rotativa automática
- Execução direta e rápida

**Uso:**
```bash
python lorenz_completo_rapido.py
```

#### 4. `lorenz_trajetoria_completa.py` 🌟 **NOVO!** (VERSÃO COMPLETA)
- **Trajetórias crescentes sem apagar**
- Menu interativo com 3 modos:
  - Trajetória completa (câmera estática)
  - Trajetória completa com rotação
  - Múltiplas trajetórias completas (efeito borboleta)

**Uso:**
```bash
python lorenz_trajetoria_completa.py
```

**Opções do menu:**
1. Trajetória completa crescente (vista estática)
2. Trajetória completa crescente com câmera rotativa
3. Múltiplas trajetórias crescentes (efeito borboleta)
0. Sair

## 📦 Dependências

```bash
pip install numpy matplotlib --break-system-packages
```

Ou usando requirements.txt:
```bash
pip install -r requirements.txt --break-system-packages
```

## 🎨 Características das Animações

### 🔄 Diferença entre versões:

**VERSÃO COM CAUDA** (lorenz_simples.py, lorenz_animado.py):
- Mostra apenas os últimos N pontos da trajetória
- A parte antiga da trajetória desaparece
- Visual mais "limpo" e dinâmico
- Melhor para ver o movimento atual
- Exemplo: mostra apenas os últimos 100 pontos

**VERSÃO COMPLETA** (lorenz_completo_rapido.py, lorenz_trajetoria_completa.py):
- **A trajetória NUNCA é apagada**
- Desenha o caminho completo desde o início
- Você vê o atrator sendo "desenhado" progressivamente
- Melhor para entender a forma completa do atrator
- Exemplo: todos os pontos do início até o atual ficam visíveis

---

### Animação Simples (com cauda)
- Uma trajetória única navegando pelo atrator
- Cauda colorida mostrando o histórico recente
- Ponto vermelho indicando posição atual
- Informações de tempo e coordenadas em tempo real
- Rotação automática da câmera para melhor visualização

### Múltiplas Trajetórias (Efeito Borboleta)
- 4 trajetórias com condições iniciais levemente diferentes
- Demonstra sensibilidade às condições iniciais
- Cores diferentes para cada trajetória
- Observe como trajetórias próximas divergem rapidamente!

### Animação com Trajetória Completa (NOVO!)
- **Trajetória crescente sem apagar nenhum ponto**
- Visualize o atrator sendo "desenhado" do início ao fim
- Câmera pode rotar automaticamente para melhor visualização
- Ponto verde marca o início, ponto vermelho mostra posição atual
- Perfeito para entender a estrutura completa do atrator
- Contador de progresso em tempo real

## 🎥 Salvando como GIF

Para criar um GIF animado:

1. Execute `python lorenz_animado.py`
2. Escolha opção 3
3. Digite o nome do arquivo (ou pressione Enter para usar o padrão)
4. Aguarde a criação (pode levar alguns minutos)

## ⚙️ Personalizações

Você pode modificar os parâmetros diretamente no código:

### Parâmetros do Sistema
```python
sigma = 10   # Número de Prandtl
rho = 28     # Número de Rayleigh
beta = 8/3   # Parâmetro geométrico
```

### Parâmetros da Animação
```python
num_passos = 5000      # Número de pontos da trajetória
dt = 0.01              # Passo de integração
intervalo = 20         # Milissegundos entre frames
tamanho_cauda = 100    # Comprimento da cauda visível
```

### Condições Iniciais
```python
x0 = 0
y0 = 1
z0 = 1.05
```

## 📊 Explicação Científica

O Atrator de Lorenz demonstra:

- **Caos Determinístico**: Equações simples produzem comportamento complexo e imprevisível
- **Sensibilidade às Condições Iniciais**: Pequenas diferenças iniciais levam a resultados drasticamente diferentes (efeito borboleta)
- **Estrutura Fractal**: O atrator possui estrutura auto-similar em diferentes escalas
- **Não-Periodicidade**: A trajetória nunca se repete exatamente

## 🎓 Aplicações

O sistema de Lorenz é usado para estudar:
- Previsão do tempo
- Dinâmica de fluidos
- Teoria do caos
- Sistemas complexos
- Lasers
- Circuitos elétricos

## 💡 Dicas de Uso

- Para melhor desempenho, use `lorenz_simples.py` em computadores mais lentos
- Reduza `num_passos` se a animação estiver lenta
- Aumente `tamanho_cauda` para ver mais histórico da trajetória
- Experimente diferentes condições iniciais para explorar diferentes partes do atrator

## 🐛 Troubleshooting

**Animação muito lenta:**
- Reduza `num_passos` para 2000-3000
- Aumente `intervalo` para 30-50
- Reduza `tamanho_cauda` para 50

**Erro de importação:**
```bash
pip install numpy matplotlib --break-system-packages
```

**Para salvar GIF (se necessário):**
```bash
pip install pillow --break-system-packages
```

## 📚 Referências

- Lorenz, E. N. (1963). "Deterministic Nonperiodic Flow". Journal of the Atmospheric Sciences.
- Strogatz, S. H. (2015). "Nonlinear Dynamics and Chaos"
- Wikipedia: [Lorenz System](https://en.wikipedia.org/wiki/Lorenz_system)

## 📄 Licença

Código livre para uso educacional e científico.

---

**Desenvolvido para demonstração do comportamento caótico em sistemas dinâmicos**

Divirta-se explorando o caos! 🦋
