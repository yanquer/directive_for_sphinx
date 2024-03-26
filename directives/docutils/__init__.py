
from docutils.parsers.rst import directives

from .figure import DocFigure


def register_doc_directives():
    directives.register_directive("figure", DocFigure)




