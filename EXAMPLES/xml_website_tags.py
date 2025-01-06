#
from lxml.builder import ElementMaker

_NS_WEBSITE_URL = "http://www.cja-tech.com/ns/websites"

_E = ElementMaker(
    namespace=_NS_WEBSITE_URL,
    nsmap={'ws': _NS_WEBSITE_URL}
)

WEBSITE = _E.website
WEBSITE_TITLE = _E.title
WEBSITE_URL = _E.url
