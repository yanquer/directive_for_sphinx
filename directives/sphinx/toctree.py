import os

from docutils import nodes
# from sphinx.directives.other import TocTree
# from sphinx import addnodes
from docutils.parsers.rst import directives
from docutils.nodes import Node

from pelican import Pelican


from ..helper import DirectiveNoHandle
from ...common import get_pelican_app, pelican_html_a_tag


def int_or_nothing(argument: str) -> int:
    if not argument:
        return 999
    return int(argument)


class SphinxTocTree(DirectiveNoHandle):
    """sphinx-toctree directive, in pelican nothing do"""

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'maxdepth': int,
        'name': directives.unchanged,
        'caption': directives.unchanged_required,
        'glob': directives.flag,
        'hidden': directives.flag,
        'includehidden': directives.flag,
        'numbered': int_or_nothing,
        'titlesonly': directives.flag,
        'reversed': directives.flag,
    }

    def each_link_node(self, content_root: str, cur_file: str, content_name: str):
        """
            Convert echo name to a {filename} link
        """
        cur_dir = os.path.dirname(cur_file)

        if content_name.endswith("*") or content_name.endswith("*/"):
            if not "glob" in self.options:
                raise RuntimeError("cannot find glob with * pattern in .. toctree")
            content_name = content_name.removesuffix("/")
            content_name = content_name.removesuffix("*")
            find_dir_name = os.path.join(cur_dir, content_name)
            if not os.path.isdir(find_dir_name):
                raise RuntimeError("cant not use * with not a directory in .. toctree")
            all_glob = [pelican_html_a_tag(content_name + "/" + x, x) for x in os.listdir(find_dir_name) if x != content_name]
            return "\n".join(all_glob)

        return pelican_html_a_tag(content_name, content_name)

    def run(self) -> list[Node]:
        # if not self.content or not self.content.data:
        #     return super().run()

        document = self.state.document
        current_file: str = document.current_source

        app: Pelican = get_pelican_app()
        all_link = [self.each_link_node(app.path, current_file, link_name) for link_name in self.content.data if link_name]
        parse_content = "\n".join(all_link)
        return [nodes.raw("", parse_content, format="html")]


