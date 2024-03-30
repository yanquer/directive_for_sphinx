import re, os, sys

from docutils.parsers.rst.directives.images import Figure

from ...common import get_pelican_app


class DocFigure(Figure):
    """
        auto convert relative-path to absolute-path
    """

    has_content = True

    # 将 ../ 前缀全部去除
    # re.compile(r'^(\.\./*)*').sub("", "..//../qw/../12")
    _relative_pattern = re.compile(r'^(\.\./*)*')

    def run(self):
        app = get_pelican_app()
        images_paths = app.settings.get("STATIC_PATHS", [])
        content_path = app.settings.get("PATH", "content")
        if (arg0 := self.arguments[0]) and arg0.startswith("../"):
            arg0 = self._relative_pattern.sub("", arg0)

            for one_static in images_paths:
                # one_static: str
                # 使用上一层, 因为会与给的参数的第一个重合
                one_static_dir = os.path.dirname(one_static)
                if sys.platform == "win32":
                    # 浏览器使用的路径是正斜杠, 不区分平台. 但是为了兼容其他平台可能存在其他情况, 仅单独处理
                    output_img = f"{one_static_dir}/{arg0}"
                else:
                    output_img = os.path.join(one_static_dir, arg0)
                img = os.path.join(content_path, one_static_dir, arg0)
                if os.path.exists(img):
                    self.arguments[0] = output_img
                    break

        if app.settings.get("IMAGE_AUTO_ALT", False) and \
            "alt" not in self.options:
            self.options["alt"] = "as you see"


        result = super().run()

        return result
