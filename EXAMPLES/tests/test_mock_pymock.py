import pytest  # Needed for test runner
from spamlib import spam

SEARCH_TERM = 'bug'
SEARCH_STRING = 'lightning bug'

def test_spam_search_calls_re_search(mocker):   # Unit test
    # Patch re.search (i.e., replace re.search with a Mock object that 
    # records calls to it)
    mocker.patch('spamlib.spam.re.search')  
    
    s = spam.SpamSearch(SEARCH_TERM, SEARCH_STRING)  # Create instance of SpamSearch
    s.findit()   # Call the method under test

    # Check that method was called just once with the expected parameters
    spam.re.search.assert_called_once_with(SEARCH_TERM, SEARCH_STRING)  


if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])   # Start the test runner
