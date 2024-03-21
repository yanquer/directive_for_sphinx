
from docutils.parsers.rst import roles

from .sphinx_roles import doc_role, ref_role, download_role


def setup_all_roles(app):
    roles.register_local_role('doc', doc_role)
    roles.register_local_role('ref', ref_role)
    roles.register_local_role('download', download_role)

