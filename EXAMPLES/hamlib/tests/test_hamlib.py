import pytest
from hamlib import Hamlib, sample_function

@pytest.fixture
def Hamlib_object():
    obj = Hamlib()
    return obj

def test_Hamlib_instance_has_sample_method(Hamlib_object):
    assert hasattr(Hamlib_object, "sample_method")

def test_hamlib_has_sample_function():
    assert sample_function() is None  # no return value
