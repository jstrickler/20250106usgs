import pytest

@pytest.mark.ex1
def test_one():
    assert True

@pytest.mark.ex2
def test_two():
    assert True

@pytest.mark.ex3
def test_three():
    assert True

@pytest.mark.ex4
def test_four():
    assert True

@pytest.mark.foo1
def test_five():
    assert True

@pytest.mark.foo2
def test_six():
    assert True

if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])   # Start the test runner