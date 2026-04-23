"""
Test suite para validação do ambiente de Data Science.

Este módulo valida:
- Instalação de bibliotecas essenciais
- Disponibilidade de ferramentas CLI
- Funcionamento básico das principais libs

Objetivo:
Garantir que o ambiente está pronto para uso em análises,
ETL e experimentação com dados.
"""

import pytest
# pylint: disable=import-outside-toplevel
import importlib
import subprocess


# =========================
# Teste de instalação (libs Python)
# =========================

LIBS = [
    ("pandas", "DataFrame"),
    ("numpy", "array"),
    ("scipy.stats", "norm"),
    ("statsmodels.api", "OLS"),
    ("sklearn.datasets", "load_iris"),
    ("matplotlib.pyplot", "plot"),
    ("seaborn", "set_theme"),
    ("polars", "DataFrame"),
    ("ipykernel", "__version__"),
]


@pytest.mark.parametrize("lib, attr", LIBS)
def test_lib_installed(lib, attr):
    """
    Verifica se uma biblioteca está instalada e expõe um atributo esperado.

    Args:
        lib (str): Nome do módulo a ser importado.
        attr (str): Nome do atributo esperado dentro do módulo.

    Raises:
        AssertionError: Caso o atributo não exista no módulo.
    """
    module = importlib.import_module(lib)
    assert hasattr(module, attr), f"{lib} não possui atributo {attr}"


# =========================
# Teste de ferramentas CLI
# =========================

CLI_TOOLS = ["ruff", "black", "jupyter-lab"]


@pytest.mark.parametrize("tool", CLI_TOOLS)
def test_cli_tools_installed(tool):
    """
    Verifica se ferramentas CLI estão disponíveis no ambiente.

    Args:
        tool (str): Nome do comando CLI.

    Raises:
        subprocess.CalledProcessError: Caso o comando falhe ou não exista.
    """
    subprocess.run([tool, "--version"], capture_output=True, check=True)


# =========================
# Teste de funcionalidade
# =========================

class TestLibsFunctionality:
    """
    Executa testes básicos de funcionalidade das bibliotecas.

    Esses testes atuam como "smoke tests", garantindo que:
    - As libs importam corretamente
    - Operações simples funcionam
    """

    def test_pandas_basic_operation(self):
        """Valida criação e estrutura de DataFrame com pandas."""
        import pandas as pd

        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert df.shape == (3, 2)
        assert list(df.columns) == ["A", "B"]

    def test_numpy_basic_operation(self):
        """Valida criação de array e cálculo de média com numpy."""
        import numpy as np

        arr = np.array([1, 2, 3, 4, 5])
        assert np.allclose(arr.mean(), 3.0)
        assert arr.shape == (5,)

    def test_scipy_basic_operation(self):
        """Valida cálculo de densidade de probabilidade com scipy."""
        from scipy import stats

        result = stats.norm.pdf(0)
        assert isinstance(result, float)
        assert result > 0

    def test_statsmodels_basic_operation(self):
        """Valida ajuste de regressão linear com statsmodels."""
        import statsmodels.api as sm
        import numpy as np

        X = np.arange(10)
        y = 2 * X + 1

        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()

        assert model is not None
        assert len(model.params) == 2

    def test_sklearn_basic_operation(self):
        """
        Valida carregamento do dataset Iris com sklearn.

        Usa tipagem explícita (cast) para evitar problemas com Pylance,
        garantindo acesso seguro ao atributo `.data`.
        """
        from sklearn.datasets import load_iris
        from sklearn.utils import Bunch
        from typing import cast

        iris = cast(Bunch, load_iris())
        assert iris.data.shape == (150, 4)  # pylint: disable=no-member

    def test_matplotlib_basic_operation(self):
        """Valida criação de figura com matplotlib."""
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        assert fig is not None
        assert ax is not None
        plt.close(fig)

    def test_seaborn_basic_operation(self):
        """Valida criação de gráfico simples com seaborn."""
        import seaborn as sns
        import pandas as pd

        df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
        sns.lineplot(data=df, x="x", y="y")
        assert df is not None

    def test_polars_basic_operation(self):
        """Valida criação de DataFrame com polars."""
        import polars as pl

        df = pl.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert df.shape == (3, 2)


# =========================
# Entry point opcional
# =========================

if __name__ == "__main__":
    """
    Permite executar os testes diretamente via Python.

    Exemplo:
        python test_libs_installed.py
    """
    pytest.main([__file__, "-v", "--tb=short"])
