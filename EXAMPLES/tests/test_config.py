
def test_stdout():  # unit test that writes to STDOUT
    print("WHOOPEE", end=" ")
    assert 1


def test_two(common_fixture):   # unit test that uses fixture from conftest.py
    assert "alpha" in common_fixture
    assert "beta" in common_fixture
    assert "gamma" in common_fixture
