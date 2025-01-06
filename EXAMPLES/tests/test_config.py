import pytest


def test_stdout():  # unit test that writes to STDOUT
    print("WHOOPEE", end=" ")
    assert 1


def test_two(common_fixture):   # unit test that uses fixture from conftest.py
    assert "alpha" in common_fixture
    assert "beta" in common_fixture
    assert "gamma" in common_fixture


if __name__ == '__main__':
    pytest.main([__file__, "-s"])   # run tests (without stdout/stderr capture) when this script is run

