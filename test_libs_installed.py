"""
Testes para verificação de instalação e funcionalidade das bibliotecas do projeto
"""

import pytest
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
    """Verifica se biblioteca está instalada e possui atributo esperado"""
    module = importlib.import_module(lib)
    assert hasattr(module, attr), f"{lib} não possui atributo {attr}"


# =========================
# Teste de ferramentas CLI
# =========================

CLI_TOOLS = ["ruff", "black", "jupyter-lab"]


@pytest.mark.parametrize("tool", CLI_TOOLS)
def test_cli_tools_installed(tool):
    """Verifica se ferramentas CLI estão disponíveis"""
    result = subprocess.run([tool, "--version"], capture_output=True)
    assert result.returncode == 0, f"{tool} não está disponível"


# =========================
# Teste de funcionalidade
# =========================

class TestLibsFunctionality:
    """Testa funcionalidades básicas das bibliotecas"""

    def test_pandas_basic_operation(self):
        import pandas as pd
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert df.shape == (3, 2)
        assert list(df.columns) == ["A", "B"]

    def test_numpy_basic_operation(self):
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        assert np.allclose(arr.mean(), 3.0)
        assert arr.shape == (5,)

    def test_scipy_basic_operation(self):
        from scipy import stats
        result = stats.norm.pdf(0)
        assert isinstance(result, float)
        assert result > 0

    def test_statsmodels_basic_operation(self):
        import statsmodels.api as sm
        import numpy as np

        X = np.arange(10)
        y = 2 * X + 1

        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()

        assert model is not None
        assert len(model.params) == 2

    def test_sklearn_basic_operation(self):
        from sklearn.datasets import load_iris
        iris = load_iris()
        assert iris.data.shape == (150, 4)

    def test_matplotlib_basic_operation(self):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        assert fig is not None
        assert ax is not None
        plt.close(fig)

    def test_seaborn_basic_operation(self):
        import seaborn as sns
        import pandas as pd

        df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
        sns.lineplot(data=df, x="x", y="y")
        assert df is not None

    def test_polars_basic_operation(self):
        import polars as pl
        df = pl.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        assert df.shape == (3, 2)


# =========================
# Entry point opcional
# =========================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])