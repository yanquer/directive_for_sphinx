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

from docutils import nodes


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


def doc_role(*args):
    return only_emphasis_role(*args)


def ref_role(*args):
    return only_emphasis_role(*args)


def download_role(*args):
    return only_emphasis_role(*args)



