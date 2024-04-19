import pytest
import pyqpo

@pytest.fixture(scope="session")
def test_lightcurve_path():
    return (
        pyqpo.__path__[0] +
        "resources/r1156_fin.dat"
    )


@pytest.fixture(scope="session")
def test_lightcurve_data(test_lightcurve_path):
    from numpy import loadtxt
    return loadtxt(test_lightcurve_path)
