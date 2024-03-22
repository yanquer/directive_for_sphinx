from docutils import nodes

from pelican import Pelican


class GlobalPelicanApp(object):

    current: Pelican = None


def get_pelican_app():
    return GlobalPelicanApp.current


def init_need_env(app: Pelican):
    GlobalPelicanApp.current = app


def doc_util_reference(href: str, name: str):
    # 构造一个 reference 节点
    ref_node = nodes.reference()
    ref_node['refuri'] = href  # 设置链接的目标 URL
    ref_node.append(nodes.Text(name))  # 设置显示文本
    return ref_node


def html_a_tag_with_div(href: str, name: str):
    return '<div>' + html_a_tag(href, name) + '</div>'


def html_a_tag(href: str, name: str):
    return '<a class="sphinx-toc-tree" href=\"' + href + '\">' + name + '</>'


def pelican_html_a_tag(href: str, name: str, div=False):
    if not href.startswith('{filename}'):
        if not href.startswith('/') and not href.startswith('./'):
            href = "./" + href
        href = '{filename}' + href
    if not href.endswith(".rst"):
        href += ".rst"
    for mat in ("/index", ".rst"):
        if name.endswith(mat):
            name = name.removesuffix(mat)
    return html_a_tag(href, name) if not div else html_a_tag_with_div(href, name)



