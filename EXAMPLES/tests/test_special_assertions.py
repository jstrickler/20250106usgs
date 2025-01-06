import pytest
import math

FILE_NAME = 'IDONOTEXIST.txt'


# subject under test ####################################
def read_file_data(file_name):
    with open(file_name) as file_in:
        data = file_in.read().splitlines()
        return data
#########################################################


def test_missing_filename():
    """
    Assert FileNotFoundError is raised
    """
    with pytest.raises(FileNotFoundError):
        read_file_data(FILE_NAME)  # will pass test if file is NOT found


def test_list():
    # fail unless values are within 0.000001 of each other
    # (actual result is 0.30000000000000004)
    assert (.1 + .2) == pytest.approx(.3)
 

def test_approximate_pi():
    # Default tolerance is 0.000001
    # smaller (or larger) tolerance can be specified
    assert 22 / 7 == pytest.approx(math.pi, .001)

if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])   # Start the test runner