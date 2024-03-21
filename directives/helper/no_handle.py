

from docutils import nodes, utils
from docutils.parsers.rst import Directive, directives, roles


class SphinxNoHandle(Directive):
    """nothing do"""

    def run(self):
        return [nodes.raw("", "", format="html")]


