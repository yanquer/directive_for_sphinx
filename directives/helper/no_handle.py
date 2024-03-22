

from docutils import nodes, utils
from docutils.parsers.rst import Directive, directives, roles


class SphinxNoHandle(Directive):
    """nothing do"""

    def run(self):
        return [nodes.raw("", "", format="html")]

    def get_settings(self):
        """
            Return pelican and doc-util settings
        """
        return self.state.document.settings


