
from pelican.rstdirectives import Pygments
import pelican.settings as pys

from docutils.parsers.rst import Directive, directives, roles
from docutils import nodes, utils

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import TextLexer, get_lexer_by_name

from ..helper.no_handle import SphinxNoHandle


class SphinxCodeBlock(Pygments):

    required_arguments = 0
    optional_arguments = 1
    option_spec = Pygments.option_spec.copy()
    option_spec["caption"] = directives.unchanged
    option_spec["emphasize-lines"] = directives.unchanged
    option_spec["name"] = directives.unchanged

    def get_lexer(self):
        try:
            if self.arguments:
                lexer = get_lexer_by_name(self.arguments[0])
            else:
                lexer = TextLexer()
        except ValueError:
            # no lexer found - use the text one instead of an exception
            lexer = TextLexer()
        return lexer

    def run(self):
        self.assert_has_content()
        lexer = self.get_lexer()

        # Fetch the defaults
        if pys.PYGMENTS_RST_OPTIONS is not None:
            for k, v in pys.PYGMENTS_RST_OPTIONS.items():
                # Locally set options overrides the defaults
                if k not in self.options:
                    self.options[k] = v

        if "linenos" in self.options and self.options["linenos"] not in (
            "table",
            "inline",
        ):
            if self.options["linenos"] == "none":
                self.options.pop("linenos")
            else:
                self.options["linenos"] = "table"

        for flag in ("nowrap", "nobackground", "anchorlinenos"):
            if flag in self.options:
                self.options[flag] = True

        # noclasses should already default to False, but just in case...
        formatter = HtmlFormatter(noclasses=False, **self.options)
        parsed = highlight("\n".join(self.content), lexer, formatter)
        return [nodes.raw("", parsed, format="html")]






