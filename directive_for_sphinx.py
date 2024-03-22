

from pelican.plugins import signals
from pelican import Pelican

from .directives import register_all_directives
from .common import init_need_env
from .roles import setup_all_roles


def init_do(app: Pelican):
    init_need_env(app)
    setup_all_roles(app)


def register():
    register_all_directives()

    signals.initialized.connect(init_do)


