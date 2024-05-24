
from docutils import nodes, utils
from docutils.parsers.rst.directives.body import BasePseudoSection
from docutils.parsers.rst import Directive, directives

from ...directives.helper import DirectiveNoHandle


class SphinxFunction(DirectiveNoHandle):

    required_arguments = 0
    optional_arguments = 1
    # 如果包含空格, 会被识别为多个参数
    # optional_arguments = 100

    final_argument_whitespace = True
    has_content = True

    option_spec = {
        'return': directives.unchanged,
        'param': directives.unchanged_required,
        'noindex': directives.flag,
    }

    def run(self):
        self.assert_has_content()

        fun_name = ""
        if self.arguments:
            fun_name = self.arguments[0]

        function_node = nodes.section(ids=[fun_name])
        function_node['classes'].append("rst-function")
        title = nodes.strong(text=fun_name)
        function_node += title

        function_return = self.options.get('return', '')
        function_params = self.options.get('param', '')

        if function_return:
            return_node = nodes.paragraph(text=f"Returns: {function_return}")
            function_node += return_node

        if function_params:
            params_node = nodes.paragraph(text=f"Parameters: {function_params}")
            function_node += params_node

        function_content = '\n'.join(self.content)
        # 原样输出. 比如 code
        # function_body = nodes.literal_block(function_content, function_content)
        function_body = nodes.paragraph(function_content)
        function_node += function_body
        self.state.nested_parse(self.content, self.content_offset,
                                function_node)

        return [function_node]





