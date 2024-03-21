
from docutils.parsers.rst import directives

from .toctree import SphinxTocTree
from .sp_function import SphinxFunction
from .literalinclude import SphinxLiteralInclude
from .code_block import SphinxCodeBlock


def register_sphinx_directives():
    directives.register_directive("toctree", SphinxTocTree)
    directives.register_directive("function", SphinxFunction)
    directives.register_directive("literalinclude", SphinxLiteralInclude)
    directives.register_directive("code-block", SphinxCodeBlock)




