"""
╔══════════════════════════════════════════════════════════════╗
║        ALGORITMO DE HUFFMAN — Interface Gráfica Python       ║
║        Biblioteca: tkinter (padrão do Python 3)              ║
╚══════════════════════════════════════════════════════════════╝

Para executar:
    python huffman_gui.py
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import heapq
from collections import Counter


# ════════════════════════════════════════════════════
#   ALGORITMO DE HUFFMAN
# ════════════════════════════════════════════════════

class No:
    """Nó da árvore de Huffman."""
    def __init__(self, caractere, frequencia):
        self.caractere  = caractere
        self.frequencia = frequencia
        self.esquerda   = None
        self.direita    = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia


def contar_frequencias(texto: str) -> dict:
    return dict(Counter(texto))


def construir_arvore(frequencias: dict) -> No:
    heap = [No(ch, freq) for ch, freq in frequencias.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        esq = heapq.heappop(heap)
        dir = heapq.heappop(heap)
        interno = No(None, esq.frequencia + dir.frequencia)
        interno.esquerda = esq
        interno.direita  = dir
        heapq.heappush(heap, interno)
    return heap[0]


def gerar_codigos(no: No, prefixo="", tabela=None) -> dict:
    if tabela is None:
        tabela = {}
    if no:
        if no.caractere is not None:
            tabela[no.caractere] = prefixo or "0"
        else:
            gerar_codigos(no.esquerda, prefixo + "0", tabela)
            gerar_codigos(no.direita,  prefixo + "1", tabela)
    return tabela


def codificar(texto: str, tabela: dict) -> str:
    return "".join(tabela[ch] for ch in texto)


def decodificar(bits: str, raiz: No) -> str:
    resultado, no_atual = [], raiz
    for bit in bits:
        no_atual = no_atual.esquerda if bit == "0" else no_atual.direita
        if no_atual.caractere is not None:
            resultado.append(no_atual.caractere)
            no_atual = raiz
    return "".join(resultado)


# ════════════════════════════════════════════════════
#   DESENHO DA ÁRVORE NO CANVAS
# ════════════════════════════════════════════════════

NODE_R   = 24   # raio dos nós internos
LEAF_W   = 50   # largura dos nós folha
LEAF_H   = 38   # altura dos nós folha
V_GAP    = 80   # espaço vertical entre níveis
H_GAP    = 56   # espaço horizontal mínimo entre folhas


def _calcular_posicoes(no, depth=0, contador=None):
    """Atribui coordenadas (x, y) a cada nó por travessia in-order."""
    if contador is None:
        contador = [0]
    if no is None:
        return
    if no.esquerda is None and no.direita is None:   # folha
        no._x = contador[0] * H_GAP + H_GAP // 2
        no._y = depth * V_GAP + NODE_R + 10
        contador[0] += 1
    else:
        _calcular_posicoes(no.esquerda, depth + 1, contador)
        _calcular_posicoes(no.direita,  depth + 1, contador)
        no._x = (no.esquerda._x + no.direita._x) // 2
        no._y = depth * V_GAP + NODE_R + 10


def _largura_arvore(no):
    if no is None:
        return 0
    if no.esquerda is None and no.direita is None:
        return 1
    return _largura_arvore(no.esquerda) + _largura_arvore(no.direita)


def _profundidade_arvore(no):
    if no is None:
        return 0
    return 1 + max(_profundidade_arvore(no.esquerda),
                   _profundidade_arvore(no.direita))


def desenhar_arvore(canvas: tk.Canvas, raiz: No):
    canvas.delete("all")
    if raiz is None:
        return

    _calcular_posicoes(raiz)

    largura = _largura_arvore(raiz)
    prof    = _profundidade_arvore(raiz)
    w = largura * H_GAP + 40
    h = prof    * V_GAP + 80
    canvas.config(scrollregion=(0, 0, w, h))

    COR_INTERNO = "#1e2d3d"
    COR_FOLHA   = "#0d2137"
    COR_BORDA   = "#00c8e0"
    COR_FOLHA_B = "#ff7043"
    COR_ARESTA  = "#334455"
    COR_TEXTO   = "#e0f0ff"
    COR_FREQ    = "#607d8b"
    COR_0       = "#546e7a"
    COR_1       = "#43a047"

    def desenhar_no(no):
        if no is None:
            return

        # Arestas
        if no.esquerda:
            canvas.create_line(no._x, no._y, no.esquerda._x, no.esquerda._y,
                                fill=COR_ARESTA, width=1, dash=(4, 3))
            mx = (no._x + no.esquerda._x) // 2
            my = (no._y + no.esquerda._y) // 2
            canvas.create_text(mx - 8, my, text="0", fill=COR_0, font=("Courier", 9, "bold"))
        if no.direita:
            canvas.create_line(no._x, no._y, no.direita._x, no.direita._y,
                                fill=COR_ARESTA, width=1, dash=(4, 3))
            mx = (no._x + no.direita._x) // 2
            my = (no._y + no.direita._y) // 2
            canvas.create_text(mx + 8, my, text="1", fill=COR_1, font=("Courier", 9, "bold"))

        if no.caractere is not None:
            # Nó folha — retângulo
            x, y = no._x, no._y
            hw, hh = LEAF_W // 2, LEAF_H // 2
            canvas.create_rectangle(x - hw, y - hh, x + hw, y + hh,
                                     fill=COR_FOLHA, outline=COR_FOLHA_B, width=2)
            label = "·" if no.caractere == " " else repr(no.caractere)[1:-1]
            canvas.create_text(x, y - 7, text=label,
                                fill=COR_FOLHA_B, font=("Courier", 11, "bold"))
            canvas.create_text(x, y + 9, text=str(no.frequencia),
                                fill=COR_FREQ, font=("Courier", 9))
        else:
            # Nó interno — círculo
            x, y = no._x, no._y
            canvas.create_oval(x - NODE_R, y - NODE_R, x + NODE_R, y + NODE_R,
                                fill=COR_INTERNO, outline=COR_BORDA, width=1)
            canvas.create_text(x, y, text=str(no.frequencia),
                                fill=COR_TEXTO, font=("Courier", 10))

        desenhar_no(no.esquerda)
        desenhar_no(no.direita)

    desenhar_no(raiz)


# ════════════════════════════════════════════════════
#   INTERFACE GRÁFICA
# ════════════════════════════════════════════════════

class HuffmanApp(tk.Tk):

    # ── Paleta de cores ──
    BG         = "#0b1117"
    SURFACE    = "#111820"
    SURFACE2   = "#162030"
    BORDER     = "#1e2d3d"
    ACCENT     = "#00c8e0"
    ACCENT2    = "#ff7043"
    ACCENT3    = "#43a047"
    TEXT       = "#c8d8e8"
    TEXT_DIM   = "#4a6070"
    FONT_MONO  = ("Courier", 11)
    FONT_TITLE = ("Courier", 13, "bold")
    FONT_SMALL = ("Courier", 9)

    def __init__(self):
        super().__init__()
        self.title("Algoritmo de Huffman")
        self.geometry("1200x820")
        self.minsize(900, 640)
        self.configure(bg=self.BG)
        self._configurar_estilo()
        self._construir_ui()
        # Texto padrão
        self.entrada.insert("1.0", "algoritmo de huffman em python com interface grafica")
        self.executar()

    # ── Estilo ttk ──────────────────────────────────
    def _configurar_estilo(self):
        s = ttk.Style(self)
        s.theme_use("clam")

        s.configure("TFrame",        background=self.BG)
        s.configure("Surface.TFrame",background=self.SURFACE)
        s.configure("TLabel",        background=self.BG,       foreground=self.TEXT,    font=self.FONT_MONO)
        s.configure("Dim.TLabel",    background=self.SURFACE,  foreground=self.TEXT_DIM,font=self.FONT_SMALL)
        s.configure("Title.TLabel",  background=self.SURFACE,  foreground=self.ACCENT,  font=self.FONT_TITLE)
        s.configure("Accent.TLabel", background=self.BG,       foreground=self.ACCENT,  font=("Courier", 22, "bold"))
        s.configure("Accent2.TLabel",background=self.BG,       foreground=self.ACCENT2, font=("Courier", 22, "bold"))
        s.configure("Accent3.TLabel",background=self.BG,       foreground=self.ACCENT3, font=("Courier", 22, "bold"))
        s.configure("StatLbl.TLabel",background=self.BG,       foreground=self.TEXT_DIM,font=("Courier", 9))

        s.configure("TButton",
                    background=self.BG, foreground=self.ACCENT,
                    bordercolor=self.ACCENT, focuscolor=self.ACCENT,
                    font=("Courier", 11, "bold"), padding=(14, 6))
        s.map("TButton",
              background=[("active", self.ACCENT)],
              foreground=[("active", self.BG)])

        # Treeview (tabela de códigos)
        s.configure("Treeview",
                    background=self.SURFACE2, foreground=self.TEXT,
                    fieldbackground=self.SURFACE2, borderwidth=0,
                    font=self.FONT_MONO, rowheight=24)
        s.configure("Treeview.Heading",
                    background=self.SURFACE, foreground=self.ACCENT,
                    font=("Courier", 9, "bold"), relief="flat")
        s.map("Treeview", background=[("selected", "#1e3a4a")])

        # Scrollbars finas
        s.configure("Vertical.TScrollbar",
                    background=self.BORDER, troughcolor=self.BG,
                    borderwidth=0, arrowsize=10)
        s.configure("Horizontal.TScrollbar",
                    background=self.BORDER, troughcolor=self.BG,
                    borderwidth=0, arrowsize=10)

    # ── Construção da UI ────────────────────────────
    def _construir_ui(self):
        # ── Título ──
        header = tk.Frame(self, bg=self.BG, pady=12)
        header.pack(fill="x", padx=20)
        tk.Label(header, text="HUFFMAN CODEC",
                 bg=self.BG, fg=self.ACCENT,
                 font=("Courier", 26, "bold")).pack()
        tk.Label(header, text="visualizador interativo · python + tkinter",
                 bg=self.BG, fg=self.TEXT_DIM, font=("Courier", 10)).pack()

        separator = tk.Frame(self, bg=self.BORDER, height=1)
        separator.pack(fill="x", padx=20)

        # ── Área principal ──
        main = tk.Frame(self, bg=self.BG)
        main.pack(fill="both", expand=True, padx=12, pady=10)

        # Coluna esquerda
        col_left = tk.Frame(main, bg=self.BG, width=380)
        col_left.pack(side="left", fill="y", padx=(0, 8))
        col_left.pack_propagate(False)

        # Coluna direita
        col_right = tk.Frame(main, bg=self.BG)
        col_right.pack(side="left", fill="both", expand=True)

        self._painel_entrada(col_left)
        self._painel_stats(col_left)
        self._painel_frequencias(col_left)
        self._painel_arvore(col_right)
        self._painel_codigos_e_resultado(col_right)

    # ── Painel: Entrada ──────────────────────────────
    def _painel_entrada(self, pai):
        p = self._painel(pai, "ENTRADA DE DADOS", self.ACCENT)
        p.pack(fill="x", pady=(0, 8))
        body = tk.Frame(p, bg=self.SURFACE, padx=8, pady=8)
        body.pack(fill="x")

        self.entrada = tk.Text(body, height=4, bg="#0d1822", fg=self.TEXT,
                               insertbackground=self.ACCENT,
                               font=self.FONT_MONO, relief="flat",
                               padx=8, pady=6, wrap="word",
                               highlightthickness=1,
                               highlightbackground=self.BORDER,
                               highlightcolor=self.ACCENT)
        self.entrada.pack(fill="x")

        self.lbl_chars = tk.Label(body, text="0 caracteres",
                                  bg=self.SURFACE, fg=self.TEXT_DIM,
                                  font=self.FONT_SMALL, anchor="e")
        self.lbl_chars.pack(fill="x", pady=(2, 0))
        self.entrada.bind("<KeyRelease>", self._atualizar_contador)

        btn = ttk.Button(body, text="▶  EXECUTAR", command=self.executar)
        btn.pack(pady=(8, 0))

    # ── Painel: Stats ────────────────────────────────
    def _painel_stats(self, pai):
        frame = tk.Frame(pai, bg=self.BG)
        frame.pack(fill="x", pady=(0, 8))

        dados = [
            ("statChars",    "Chars únicos", "Accent.TLabel"),
            ("statOriginal", "Bits originais","Accent2.TLabel"),
            ("statHuffman",  "Bits Huffman",  "Accent.TLabel"),
            ("statRatio",    "Compressão",    "Accent3.TLabel"),
        ]
        for i, (attr, label, style) in enumerate(dados):
            card = tk.Frame(frame, bg=self.BG, highlightbackground=self.BORDER,
                            highlightthickness=1, padx=6, pady=6)
            card.grid(row=0, column=i, sticky="nsew", padx=3)
            frame.columnconfigure(i, weight=1)
            lbl_val = ttk.Label(card, text="—", style=style)
            lbl_val.pack()
            ttk.Label(card, text=label, style="StatLbl.TLabel").pack()
            setattr(self, attr, lbl_val)

    # ── Painel: Frequências ──────────────────────────
    def _painel_frequencias(self, pai):
        p = self._painel(pai, "FREQUÊNCIAS", self.ACCENT2)
        p.pack(fill="both", expand=True)
        body = tk.Frame(p, bg=self.SURFACE)
        body.pack(fill="both", expand=True)

        # Canvas com scrollbar para as barras
        inner = tk.Frame(body, bg=self.SURFACE)
        inner.pack(fill="both", expand=True, padx=8, pady=6)

        vsb = ttk.Scrollbar(inner, orient="vertical")
        vsb.pack(side="right", fill="y")

        self.freq_canvas = tk.Canvas(inner, bg=self.SURFACE, highlightthickness=0,
                                     yscrollcommand=vsb.set)
        self.freq_canvas.pack(fill="both", expand=True)
        vsb.config(command=self.freq_canvas.yview)

    # ── Painel: Árvore ───────────────────────────────
    def _painel_arvore(self, pai):
        p = self._painel(pai, "ÁRVORE DE HUFFMAN", self.ACCENT)
        p.pack(fill="both", expand=True, pady=(0, 8))
        body = tk.Frame(p, bg=self.SURFACE)
        body.pack(fill="both", expand=True)

        # Canvas + scrollbars
        h_sb = ttk.Scrollbar(body, orient="horizontal")
        h_sb.pack(side="bottom", fill="x")
        v_sb = ttk.Scrollbar(body, orient="vertical")
        v_sb.pack(side="right", fill="y")

        self.tree_canvas = tk.Canvas(body, bg="#090f18", highlightthickness=0,
                                     xscrollcommand=h_sb.set,
                                     yscrollcommand=v_sb.set)
        self.tree_canvas.pack(fill="both", expand=True)
        h_sb.config(command=self.tree_canvas.xview)
        v_sb.config(command=self.tree_canvas.yview)

        # Zoom com scroll do mouse
        self.tree_canvas.bind("<MouseWheel>",
            lambda e: self.tree_canvas.yview_scroll(-1 * (e.delta // 120), "units"))

    # ── Painel: Tabela de Códigos + Resultado ────────
    def _painel_codigos_e_resultado(self, pai):
        frame = tk.Frame(pai, bg=self.BG)
        frame.pack(fill="x")
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        # Tabela de Códigos
        p_cod = self._painel(frame, "TABELA DE CÓDIGOS", self.ACCENT3)
        p_cod.grid(row=0, column=0, sticky="nsew", padx=(0, 4))
        body_cod = tk.Frame(p_cod, bg=self.SURFACE)
        body_cod.pack(fill="both", expand=True)

        cols = ("char", "freq", "codigo", "bits")
        self.tree_view = ttk.Treeview(body_cod, columns=cols, show="headings", height=7)
        self.tree_view.heading("char",   text="Char")
        self.tree_view.heading("freq",   text="Freq")
        self.tree_view.heading("codigo", text="Código Huffman")
        self.tree_view.heading("bits",   text="Bits")
        self.tree_view.column("char",   width=60,  anchor="center")
        self.tree_view.column("freq",   width=50,  anchor="center")
        self.tree_view.column("codigo", width=160, anchor="w")
        self.tree_view.column("bits",   width=40,  anchor="center")

        vsb = ttk.Scrollbar(body_cod, orient="vertical", command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.tree_view.pack(fill="both", expand=True, padx=4, pady=4)
        self.tree_view.tag_configure("folha", foreground=self.ACCENT2)

        # Resultado
        p_res = self._painel(frame, "RESULTADO", self.ACCENT2)
        p_res.grid(row=0, column=1, sticky="nsew", padx=(4, 0))
        body_res = tk.Frame(p_res, bg=self.SURFACE)
        body_res.pack(fill="both", expand=True, padx=8, pady=6)

        tk.Label(body_res, text="Codificado:", bg=self.SURFACE,
                 fg=self.TEXT_DIM, font=self.FONT_SMALL).pack(anchor="w")
        self.txt_encoded = scrolledtext.ScrolledText(
            body_res, height=4, bg="#0d1822", fg=self.ACCENT3,
            font=("Courier", 10), relief="flat", wrap="word",
            state="disabled", padx=6, pady=4)
        self.txt_encoded.pack(fill="x", pady=(2, 8))

        tk.Label(body_res, text="Decodificado:", bg=self.SURFACE,
                 fg=self.TEXT_DIM, font=self.FONT_SMALL).pack(anchor="w")
        self.txt_decoded = scrolledtext.ScrolledText(
            body_res, height=4, bg="#0d1822", fg=self.TEXT,
            font=self.FONT_MONO, relief="flat", wrap="word",
            state="disabled", padx=6, pady=4)
        self.txt_decoded.pack(fill="x", pady=(2, 6))

        self.lbl_status = tk.Label(body_res, text="", bg=self.SURFACE,
                                   fg=self.ACCENT3, font=("Courier", 9, "bold"))
        self.lbl_status.pack(anchor="w")

    # ── Helper: criar painel com cabeçalho ───────────
    def _painel(self, pai, titulo, cor):
        frame = tk.Frame(pai, bg=self.SURFACE,
                         highlightbackground=self.BORDER, highlightthickness=1)
        header = tk.Frame(frame, bg=self.SURFACE, pady=5)
        header.pack(fill="x")
        dot = tk.Canvas(header, width=8, height=8, bg=self.SURFACE,
                        highlightthickness=0)
        dot.pack(side="left", padx=(8, 4))
        dot.create_oval(1, 1, 7, 7, fill=cor, outline="")
        tk.Label(header, text=titulo, bg=self.SURFACE, fg=cor,
                 font=("Courier", 9, "bold")).pack(side="left")
        sep = tk.Frame(frame, bg=self.BORDER, height=1)
        sep.pack(fill="x")
        return frame

    # ── Atualiza contador de caracteres ─────────────
    def _atualizar_contador(self, _=None):
        n = len(self.entrada.get("1.0", "end-1c"))
        self.lbl_chars.config(text=f"{n} caracteres")

    # ── EXECUTAR ─────────────────────────────────────
    def executar(self):
        texto = self.entrada.get("1.0", "end-1c")
        if not texto.strip():
            messagebox.showwarning("Atenção", "Digite um texto para comprimir.")
            return

        self._atualizar_contador()

        # ── Cálculos ──
        freq    = contar_frequencias(texto)
        raiz    = construir_arvore(freq)
        tabela  = gerar_codigos(raiz)
        bits    = codificar(texto, tabela)
        decoded = decodificar(bits, raiz)

        orig_bits = len(texto) * 8
        huff_bits = len(bits)
        ratio     = (1 - huff_bits / orig_bits) * 100

        # ── Stats ──
        self.statChars.config(text=str(len(freq)))
        self.statOriginal.config(text=str(orig_bits))
        self.statHuffman.config(text=str(huff_bits))
        self.statRatio.config(text=f"{ratio:.1f}%")

        # ── Frequências ──
        self._renderizar_frequencias(freq)

        # ── Árvore ──
        desenhar_arvore(self.tree_canvas, raiz)

        # ── Tabela de Códigos ──
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        for ch, code in sorted(tabela.items(), key=lambda x: len(x[1])):
            label = "·" if ch == " " else repr(ch)[1:-1]
            self.tree_view.insert("", "end",
                                  values=(label, freq[ch], code, len(code)),
                                  tags=("folha",))

        # ── Encoded ──
        self._set_text(self.txt_encoded, bits)

        # ── Decoded ──
        self._set_text(self.txt_decoded, decoded)

        # ── Status ──
        ok = decoded == texto
        self.lbl_status.config(
            text="✔  Decodificação verificada com sucesso!" if ok else "✘  Erro na decodificação!",
            fg=self.ACCENT3 if ok else self.ACCENT2)

    # ── Renderiza barras de frequência no canvas ─────
    def _renderizar_frequencias(self, freq: dict):
        c = self.freq_canvas
        c.delete("all")

        sortidos = sorted(freq.items(), key=lambda x: -x[1])
        max_freq  = sortidos[0][1]
        BAR_H     = 18
        PADDING   = 6
        LABEL_W   = 42
        NUM_W     = 28
        total_h   = len(sortidos) * (BAR_H + PADDING) + PADDING

        canvas_w  = c.winfo_width() or 300
        bar_area  = canvas_w - LABEL_W - NUM_W - 16

        c.config(scrollregion=(0, 0, canvas_w, total_h))

        for i, (ch, f) in enumerate(sortidos):
            y  = PADDING + i * (BAR_H + PADDING)
            label = "·SPC·" if ch == " " else repr(ch)[1:-1]

            # Rótulo do caractere
            c.create_text(LABEL_W - 4, y + BAR_H // 2,
                          text=label, anchor="e",
                          fill=self.ACCENT2, font=("Courier", 9, "bold"))

            # Trilha da barra
            c.create_rectangle(LABEL_W, y, LABEL_W + bar_area, y + BAR_H,
                                fill="#162030", outline=self.BORDER)

            # Barra
            bw = int(bar_area * f / max_freq)
            if bw > 0:
                c.create_rectangle(LABEL_W, y, LABEL_W + bw, y + BAR_H,
                                   fill=self.ACCENT, outline="")

            # Número
            c.create_text(LABEL_W + bar_area + 6, y + BAR_H // 2,
                          text=str(f), anchor="w",
                          fill=self.TEXT_DIM, font=("Courier", 9))

    # ── Helper: escrever em Text desabilitado ────────
    def _set_text(self, widget, conteudo: str):
        widget.config(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", conteudo)
        widget.config(state="disabled")


# ════════════════════════════════════════════════════
#   PONTO DE ENTRADA
# ════════════════════════════════════════════════════
if __name__ == "__main__":
    app = HuffmanApp()
    app.mainloop()
