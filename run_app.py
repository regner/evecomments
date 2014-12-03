

import os

from flask.ext.script import Manager, Shell, Server

from evecomments.app      import create_app
from evecomments.settings import DevConfig

if os.environ.get('EI_ENV') == 'prod':
    pass
    #app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)


manager = Manager(app)


def _make_context():
    """ Return context dict for a shell session so you can access. """

    return {'app': app}


manager.add_command('server', Server())
manager.add_command('shell',  Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()