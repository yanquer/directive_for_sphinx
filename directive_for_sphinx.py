

from pelican.plugins import signals
from pelican.contents import Article

from .directives import register_all_directives
from .roles import setup_all_roles

def register():
    register_all_directives()

    signals.initialized.connect(setup_all_roles)


