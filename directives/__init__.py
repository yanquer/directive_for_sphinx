
from docutils.parsers.rst import directives

from .docutils import register_doc_directives
from .sphinx import register_sphinx_directives
from .other import register_other_directives


def register_all_directives():
    register_doc_directives()
    register_sphinx_directives()
    register_other_directives()








