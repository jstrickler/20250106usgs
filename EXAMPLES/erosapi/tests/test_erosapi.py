import pytest

from erosapi.erosapi import sample_function
from erosapi.erosapi import Erosapi

@pytest.fixture
def Erosapi_object():
    return Erosapi()

def test_Erosapi_instance_has_sample_method(Erosapi_object):
    assert hasattr(Erosapi_object, "sample_method")



def test_erosapi_has_sample_function():
    assert sample_function() is None  # no return value
