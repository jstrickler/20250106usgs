#
from lxml.builder import ElementMaker

_NS_BIB_URL = "http://www.cja-tech.com/ns/bibliography"

_E = ElementMaker(
    namespace=_NS_BIB_URL,
    nsmap={'bib': _NS_BIB_URL}
)

BIBLIOGRAPHY = _E.bibliography
ENTRY = _E.entry
