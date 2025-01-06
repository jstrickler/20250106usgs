#
from lxml.builder import ElementMaker

_NS_BOOK_URL = "http://www.cja-tech.com/ns/books"

_E = ElementMaker(
    namespace=_NS_BOOK_URL,
    nsmap={'bk': _NS_BOOK_URL}
)

BOOK = _E.book
BOOK_TITLE = _E.title
BOOK_AUTHOR = _E.author
BOOK_PUB = _E.publisher
BOOK_PUB_YEAR = _E.pubyear
