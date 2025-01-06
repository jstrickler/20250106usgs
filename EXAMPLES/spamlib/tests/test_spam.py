import pytest
from spamlib.spam import Spam, sample_function

@pytest.fixture
def Spam_object():
    obj = Spam()
    return obj

def test_Spam_instance_has_sample_method(Spam_object):
    assert hasattr(Spam_object, "sample_method")

def test_spam_has_sample_function():
    assert sample_function() is None  # no return value
