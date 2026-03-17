"""
Simulação do Teorema Central do Limite com dados
=================================================
Demonstra como a distribuição das médias de lançamentos
de um dado (uniforme) converge para uma curva normal.

Dependências: numpy, matplotlib
Instalação:   pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.widgets import Slider, Button


# ── Paleta ───────────────────────────────────────────────
AZUL   = "#378ADD"
AZUL_A = "#378ADD88"
VERMELHO = "#E24B4A"
CINZA_BG = "#F8F8F6"
CINZA_TX = "#5F5E5A"


# ── Funções de simulação ──────────────────────────────────
def rolar_dados(n_lancamentos: int, n_experimentos: int) -> np.ndarray:
    """Retorna um array com a média de cada experimento."""
    lancamentos = np.random.randint(1, 7, size=(n_experimentos, n_lancamentos))
    return lancamentos.mean(axis=1)


def normal_pdf(x: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


# ── Figura principal ──────────────────────────────────────
fig = plt.figure(figsize=(11, 7), facecolor=CINZA_BG)
fig.suptitle(
    "Teorema Central do Limite — dado de 6 faces",
    fontsize=14, fontweight="bold", color="#2C2C2A", y=0.97,
)

gs = gridspec.GridSpec(
    2, 2,
    figure=fig,
    top=0.88, bottom=0.22,
    left=0.08, right=0.97,
    hspace=0.45, wspace=0.35,
)

ax_dado  = fig.add_subplot(gs[0, 0])   # histograma de 1 dado (uniforme)
ax_tcl   = fig.add_subplot(gs[0, 1])   # histograma das médias
ax_stats = fig.add_subplot(gs[1, 0])   # tabela de estatísticas
ax_info  = fig.add_subplot(gs[1, 1])   # painel informativo

for ax in [ax_dado, ax_tcl, ax_stats, ax_info]:
    ax.set_facecolor(CINZA_BG)

# ── Sliders ───────────────────────────────────────────────
ax_sl_n   = fig.add_axes([0.12, 0.13, 0.55, 0.025])
ax_sl_exp = fig.add_axes([0.12, 0.08, 0.55, 0.025])

sl_n   = Slider(ax_sl_n,   "lançamentos / exp.", 1, 100,  valinit=10,   valstep=1,   color=AZUL)
sl_exp = Slider(ax_sl_exp, "nº de experimentos", 100, 10000, valinit=1000, valstep=100, color=AZUL)

for sl in [sl_n, sl_exp]:
    sl.label.set_color(CINZA_TX)
    sl.valtext.set_color(CINZA_TX)

# Botão
ax_btn = fig.add_axes([0.78, 0.08, 0.14, 0.07])
btn = Button(ax_btn, "Simular", color="#B5D4F4", hovercolor="#85B7EB")
btn.label.set_fontsize(11)
btn.label.set_color("#042C53")


# ── Função de atualização ─────────────────────────────────
def atualizar(event=None):
    n    = int(sl_n.val)
    nexp = int(sl_exp.val)

    medias = rolar_dados(n, nexp)

    mu_obs  = medias.mean()
    std_obs = medias.std()
    mu_teo  = 3.5
    # desvio padrão teórico do dado uniforme 1–6: sqrt(35/12)
    std_teo = np.sqrt(35 / 12) / np.sqrt(n)

    bins = min(60, max(20, nexp // 40))

    # ── painel esquerdo: dado individual ──
    ax_dado.cla()
    ax_dado.set_facecolor(CINZA_BG)
    faces = np.arange(1, 7)
    prob  = np.ones(6) / 6
    ax_dado.bar(faces, prob, color=AZUL_A, edgecolor=AZUL, linewidth=0.8, width=0.6)
    ax_dado.axhline(1/6, color=VERMELHO, linewidth=1.5, linestyle="--", label="probabilidade uniforme")
    ax_dado.set_xticks(faces)
    ax_dado.set_xlabel("face do dado", fontsize=10, color=CINZA_TX)
    ax_dado.set_ylabel("probabilidade", fontsize=10, color=CINZA_TX)
    ax_dado.set_title("distribuição de 1 dado", fontsize=11, pad=6)
    ax_dado.set_ylim(0, 0.35)
    ax_dado.legend(fontsize=8, frameon=False)
    ax_dado.tick_params(colors=CINZA_TX, labelsize=9)
    for sp in ax_dado.spines.values():
        sp.set_edgecolor("#D3D1C7")

    # ── painel direito: distribuição das médias ──
    ax_tcl.cla()
    ax_tcl.set_facecolor(CINZA_BG)
    counts, edges = np.histogram(medias, bins=bins, density=True)
    centros = (edges[:-1] + edges[1:]) / 2
    largura = edges[1] - edges[0]
    ax_tcl.bar(centros, counts, width=largura * 0.95,
               color=AZUL_A, edgecolor=AZUL, linewidth=0.5, label="médias simuladas")

    x_norm = np.linspace(medias.min() - 0.2, medias.max() + 0.2, 300)
    y_norm = normal_pdf(x_norm, mu_teo, std_teo)
    ax_tcl.plot(x_norm, y_norm, color=VERMELHO, linewidth=2.2, label="normal teórica")

    titulo_n = f"distribuição das médias  (n = {n})"
    ax_tcl.set_title(titulo_n, fontsize=11, pad=6)
    ax_tcl.set_xlabel("média dos lançamentos", fontsize=10, color=CINZA_TX)
    ax_tcl.set_ylabel("densidade", fontsize=10, color=CINZA_TX)
    ax_tcl.legend(fontsize=8, frameon=False)
    ax_tcl.tick_params(colors=CINZA_TX, labelsize=9)
    for sp in ax_tcl.spines.values():
        sp.set_edgecolor("#D3D1C7")

    # ── painel de estatísticas ──
    ax_stats.cla()
    ax_stats.set_facecolor(CINZA_BG)
    ax_stats.axis("off")
    linhas = [
        ["parâmetro",         "teórico",          "observado"],
        ["média",             f"{mu_teo:.4f}",     f"{mu_obs:.4f}"],
        ["desvio padrão",     f"{std_teo:.4f}",    f"{std_obs:.4f}"],
        ["lançamentos/exp.",  str(n),              "—"],
        ["experimentos",      str(nexp),           "—"],
    ]
    tabela = ax_stats.table(
        cellText=linhas[1:],
        colLabels=linhas[0],
        cellLoc="center",
        loc="center",
        bbox=[0, 0.05, 1, 0.9],
    )
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(9.5)
    for (row, col), cell in tabela.get_celld().items():
        cell.set_edgecolor("#D3D1C7")
        cell.set_linewidth(0.5)
        if row == 0:
            cell.set_facecolor("#B5D4F4")
            cell.set_text_props(color="#042C53", fontweight="bold")
        else:
            cell.set_facecolor(CINZA_BG if row % 2 == 0 else "white")
            cell.set_text_props(color="#2C2C2A")

    ax_stats.set_title("estatísticas", fontsize=11, pad=8)

    # ── painel informativo ──
    ax_info.cla()
    ax_info.set_facecolor(CINZA_BG)
    ax_info.axis("off")
    texto = (
        "Teorema Central do Limite\n\n"
        "Dado qualquer distribuição com média μ\n"
        "e variância σ², a distribuição das\n"
        "médias de amostras de tamanho n\n"
        "converge para:\n\n"
        "    X̄ ~ N(μ,  σ²/n)\n\n"
        f"Para um dado de 6 faces:\n"
        f"  μ = 3.5\n"
        f"  σ² = 35/12 ≈ 2.9167\n\n"
        f"Com n = {n}:\n"
        f"  σ_X̄ = {std_teo:.4f}"
    )
    ax_info.text(
        0.05, 0.95, texto,
        transform=ax_info.transAxes,
        fontsize=9.5, verticalalignment="top",
        color="#2C2C2A", linespacing=1.55,
        fontfamily="monospace",
    )
    ax_info.set_title("teoria", fontsize=11, pad=8)

    fig.canvas.draw_idle()


# ── Conectar eventos e rodar ───────────────────────────────
btn.on_clicked(atualizar)
sl_n.on_changed(lambda v: None)    # sliders apenas armazenam valor
sl_exp.on_changed(lambda v: None)

# Primeira simulação ao abrir
atualizar()
plt.show()
