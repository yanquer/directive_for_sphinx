
from docutils import nodes, utils
from sphinx.directives.other import TocTree

from ..helper.no_handle import SphinxNoHandle


class SphinxTocTree(SphinxNoHandle):
    """sphinx-toctree directive, in pelican nothing do"""

    has_content = TocTree.has_content
    required_arguments = TocTree.required_arguments
    optional_arguments = TocTree.optional_arguments
    final_argument_whitespace = TocTree.final_argument_whitespace
    option_spec = TocTree.option_spec


