"""
AUTOR      : Caio Abreu Ferreira <abreuferr (a) gmail.com>
TÍTULO     : Testes unitários para a classe Bhaskara

Suite de testes para bhaskara.py usando pytest.

Para executar:
    pytest bhaskara_test.py -v

Cobertura:
    - delta()          : cálculo do discriminante
    - calcula_raizes() : todos os casos (0, 1 e 2 raízes)
    - Validação de a=0 : deve lançar ValueError
"""

import math
import pytest
import bhaskara


# ── Fixture ──────────────────────────────────────────────────────────────────

@pytest.fixture
def b():
    """Instância compartilhada de Bhaskara para todos os testes."""
    return bhaskara.Bhaskara()


# ── Testes do delta ───────────────────────────────────────────────────────────

class TestDelta:
    """Testa o cálculo do discriminante Δ = b² - 4ac."""

    def test_delta_positivo(self, b):
        # 1² - 4×1×(-6) = 1 + 24 = 25
        assert b.delta(1, 1, -6) == 25.0

    def test_delta_zero(self, b):
        # 2² - 4×1×1 = 4 - 4 = 0
        assert b.delta(1, 2, 1) == 0.0

    def test_delta_negativo(self, b):
        # 2² - 4×1×2 = 4 - 8 = -4
        assert b.delta(1, 2, 2) == -4.0


# ── Testes das raízes ─────────────────────────────────────────────────────────

class TestCalculaRaizes:
    """Testa todos os casos de calcula_raizes()."""

    def test_uma_raiz_origem(self, b):
        """x² = 0 → raiz dupla em x = 0."""
        assert b.calcula_raizes(1, 0, 0) == (1, 0.0)

    def test_uma_raiz_negativa(self, b):
        """10x² + 20x + 10 = 0 → Δ = 0 → x = -1."""
        assert b.calcula_raizes(10, 20, 10) == (1, -1.0)

    def test_duas_raizes_inteiras(self, b):
        """x² - 5x + 6 = 0 → x1 = 3, x2 = 2."""
        assert b.calcula_raizes(1, -5, 6) == (2, 3.0, 2.0)

    def test_duas_raizes_positivas(self, b):
        """x² - 3x + 2 = 0 → x1 = 2, x2 = 1."""
        assert b.calcula_raizes(1, -3, 2) == (2, 2.0, 1.0)

    def test_duas_raizes_decimais(self, b):
        """2x² - 4x + 1 = 0 → Δ = 8 → raízes decimais."""
        qtd, x1, x2 = b.calcula_raizes(2, -4, 1)
        assert qtd == 2
        assert math.isclose(x1, (4 + math.sqrt(8)) / 4, rel_tol=1e-9)
        assert math.isclose(x2, (4 - math.sqrt(8)) / 4, rel_tol=1e-9)

    def test_zero_raizes(self, b):
        """10x² + 10x + 10 = 0 → Δ < 0 → sem raízes reais."""
        assert b.calcula_raizes(10, 10, 10) == (0,)

    def test_coeficiente_a_zero_lanca_erro(self, b):
        """a=0 torna a equação linear; deve lançar ValueError."""
        with pytest.raises(ValueError, match="'a' não pode ser zero"):
            b.calcula_raizes(0, 2, 1)
