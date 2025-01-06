import pytest
from temperature import c2f, f2c


test_data_c2f = [(100, 212),(0, 32),(37, 98.6),(-40,-40)]
test_data_f2c = [(y, x) for x, y in test_data_c2f]


@pytest.mark.parametrize("input, result", test_data_c2f)
def test_c2f(input, result):
    assert pytest.approx(c2f(input)) == result


@pytest.mark.parametrize("input, result", test_data_f2c)
def test_f2c(input, result):
    assert pytest.approx(f2c(input)) == result


