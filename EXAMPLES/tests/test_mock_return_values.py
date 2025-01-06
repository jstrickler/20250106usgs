import pytest
from unittest.mock import Mock

RETURN_VALUE = 99

ham = Mock(return_value=RETURN_VALUE)  # Spam constructor relies on ham()





# dependency to be mocked -- not used in test
# def ham():
#     return 42


if __name__ == '__main__':
    pytest.main([__file__])
