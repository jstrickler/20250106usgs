import pytest
from carddeck import Carddeck, sample_function

@pytest.fixture
def Carddeck_object():
    obj = Carddeck()
    return obj

def test_Carddeck_instance_has_sample_method(Carddeck_object):
    assert hasattr(Carddeck_object, "sample_method")

def test_carddeck_has_sample_function():
    assert sample_function() is None  # no return value
