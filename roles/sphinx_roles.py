"""
# 在这里定义您的角色解析逻辑
# name: 角色名称 ('doc')
# rawtext: 原始文本（例如：':doc:`xxx`'）
# text: 角色文本（例如：'xxx'）
# lineno: 行号
# inliner: docutils.parsers.rst.states.Inliner 对象
# options: 角色选项
# content: 内容列表
# 返回一个包含解析结果的元组，例如：(nodes, messages)
# 其中，nodes 是一个 docutils.nodes.Node 对象列表，表示解析后的内容
# messages 是一个 docutils.statemachine.Reporter 对象，用于输出解析过程中的消息
# 可以参考 docutils.parsers.rst.roles.custom_role 函数的实现
"""

import os
import re

from docutils import nodes
from pelican import Pelican

from ..common import get_pelican_app, doc_util_reference


def only_emphasis_role(role, rawtext, text, lineno, inliner, options=None, content=None):
    """
    role：角色名称的字符串
    rawtext：角色标记中的原始文本
    text：角色标记中的文本内容
    """
    if content is None:
        content = []
    if options is None:
        options = {}
    node = nodes.emphasis(rawtext, text)
    return [node], []


def doc_role(role, rawtext, text: str, lineno, inliner, options=None, content=None):
    if content is None:
        content = []
    if options is None:
        options = {}
    if role != "doc":
        return only_emphasis_role(role, rawtext, text, lineno, inliner, options, content)

    app: Pelican = get_pelican_app()

    name = None
    if "<" in text and ">" in text:
        s, e = text.index("<"), text.rindex(">")
        if s < e:
            name, text = text[:s], text[s+1:e]

    sphinx_relative_path = app.settings.get("SPHINX_RELATIVE_PATH", "")
    pelican_content_path: str = app.settings.get("PATH", "")

    cur_file = inliner.document.current_source
    cur_dir = os.path.dirname(cur_file)
    file_name = os.path.basename(cur_file)
    if name:
        _, ext = os.path.splitext(file_name)
    else:
        name, ext = os.path.splitext(file_name)

    if text.startswith('/'):
        # 先看看不加 SPHINX_RELATIVE_PATH 有没有, 没有再加
        doc_real_path: str = os.path.join(pelican_content_path, text[1:])
        if os.path.exists(doc_real_path + "" if doc_real_path.endswith(".rst") else ".rst"):
            ...
        else:
            # 没有就说明在旧的下面
            doc_real_path: str = os.path.join(pelican_content_path, sphinx_relative_path, text[1:])
        doc_url = "{filename}./" + os.path.relpath(doc_real_path, cur_dir)
    else:
        doc_real_path = os.path.join(cur_dir, text)
        doc_url = "{filename}./" + text
    if not doc_url.endswith(".rst"):
        doc_url += ".rst"

    # 构造一个 reference 节点
    # ref_node = nodes.reference()
    # ref_node['refuri'] = doc_url  # 设置链接的目标 URL
    # ref_node.append(nodes.Text(name))  # 设置显示文本

    return [doc_util_reference(doc_url, name)], []


def ref_role(*args):
    return only_emphasis_role(*args)


def download_role(*args):
    return only_emphasis_role(*args)



