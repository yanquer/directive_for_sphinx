
from docutils.parsers.rst import directives

from .post import Post


def register_other_directives():
    directives.register_directive("post", Post)




