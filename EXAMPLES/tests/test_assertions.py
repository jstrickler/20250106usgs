import pytest

def test_two_plus_two_equals_four():
    assert 2 + 2 == 4

if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])   # Start the test runner