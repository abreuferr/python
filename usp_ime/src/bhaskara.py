"""
AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO     : Equação do Segundo Grau — Fórmula de Bhaskara (OOP)

Resolve equações quadráticas na forma ax² + bx + c = 0 usando a
Fórmula de Bhaskara, encapsulada em uma classe para facilitar testes
e reutilização.

Fórmulas:
    Δ = b² - 4ac
    x = (-b ± √Δ) / (2a)

Convenção de retorno de calcula_raizes():
    (0,)        →  nenhuma raiz real (Δ < 0)
    (1, x1)     →  uma raiz real dupla (Δ = 0)
    (2, x1, x2) →  duas raízes reais distintas (Δ > 0)
"""

import math


class Bhaskara:
    """Resolve equações quadráticas ax² + bx + c = 0 via Fórmula de Bhaskara."""

    # ── Cálculo do discriminante ─────────────────────────────────────────────

    def delta(self, a: float, b: float, c: float) -> float:
        """
        Calcula o discriminante Δ = b² - 4ac.

        Parâmetros:
            a, b, c (float): Coeficientes da equação quadrática.

        Retorna:
            float: Valor do discriminante.

        Exemplos:
            >>> Bhaskara().delta(1, -5, 6)
            1.0
            >>> Bhaskara().delta(1, 2, 1)
            0.0
        """
        return b ** 2 - 4 * a * c

    # ── Resolução das raízes ─────────────────────────────────────────────────

    def calcula_raizes(
        self, a: float, b: float, c: float
    ) -> tuple:
        """
        Calcula as raízes reais de ax² + bx + c = 0.

        Convenção de retorno:
            (0,)        →  Δ < 0: nenhuma raiz real
            (1, x1)     →  Δ = 0: uma raiz dupla
            (2, x1, x2) →  Δ > 0: duas raízes distintas (x1 ≥ x2)

        Parâmetros:
            a (float): Coeficiente quadrático (deve ser ≠ 0).
            b (float): Coeficiente linear.
            c (float): Termo independente.

        Retorna:
            tuple: Conforme a convenção acima.

        Lança:
            ValueError: Se a == 0 (não seria equação quadrática).

        Exemplos:
            >>> Bhaskara().calcula_raizes(1, 0, 0)
            (1, 0.0)
            >>> Bhaskara().calcula_raizes(1, -5, 6)
            (2, 3.0, 2.0)
            >>> Bhaskara().calcula_raizes(10, 10, 10)
            (0,)
        """
        if a == 0:
            raise ValueError(
                "O coeficiente 'a' não pode ser zero (seria equação linear)."
            )

        d = self.delta(a, b, c)

        if d < 0:
            # Nenhuma raiz real: discriminante negativo implica raízes complexas
            return (0,)

        if d == 0:
            # Raiz dupla: x1 = x2 = -b / (2a)
            x1 = -b / (2 * a)
            return (1, x1)

        # Duas raízes reais distintas
        raiz_d = math.sqrt(d)
        x1 = (-b + raiz_d) / (2 * a)
        x2 = (-b - raiz_d) / (2 * a)
        return (2, x1, x2)

    # ── Interface com o usuário ──────────────────────────────────────────────

    def _coletar_coeficiente(self, nome: str) -> float:
        """
        Solicita um coeficiente ao usuário com validação de entrada.

        Parâmetros:
            nome (str): Nome do coeficiente (ex: 'a', 'b', 'c').

        Retorna:
            float: Valor numérico informado pelo usuário.
        """
        while True:
            try:
                return float(input(f"  Valor de {nome}: "))
            except ValueError:
                print(f"  Entrada inválida. '{nome}' deve ser um número.\n")

    def main(self) -> None:
        """
        Interface interativa: coleta os coeficientes, resolve a equação
        e exibe o resultado de forma descritiva.
        """
        print("=== EQUAÇÃO DO SEGUNDO GRAU ===")
        print("       ax² + bx + c = 0\n")

        # Coleta 'a' garantindo que seja diferente de zero
        while True:
            a = self._coletar_coeficiente("a")
            if a != 0:
                break
            print("  'a' não pode ser zero. Tente novamente.\n")

        b = self._coletar_coeficiente("b")
        c = self._coletar_coeficiente("c")

        print(f"\nEquação: ({a})x² + ({b})x + ({c}) = 0")
        print(f"Δ = {self.delta(a, b, c):.4f}\n")

        resultado = self.calcula_raizes(a, b, c)

        if resultado[0] == 0:
            print("Nenhuma raiz real (Δ < 0 → raízes complexas).")
        elif resultado[0] == 1:
            print(f"Uma raiz real dupla:")
            print(f"  x1 = x2 = {resultado[1]:.4f}")
        else:
            print(f"Duas raízes reais distintas:")
            print(f"  x1 = {resultado[1]:.4f}")
            print(f"  x2 = {resultado[2]:.4f}")


# ── Execução principal ───────────────────────────────────────────────────────

if __name__ == "__main__":
    Bhaskara().main()