

import os

from flask.ext.script  import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

from evecomments.app        import create_app
from evecomments.settings   import DevConfig
from evecomments.extensions import db

if os.environ.get('EI_ENV') == 'prod':
    pass
    #app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)


migrate = Migrate(app, db)
manager = Manager(app)


def _make_context():
    """ Return context dict for a shell session so you can access. """

    return {'app': app}


manager.add_command('server',     Server())
manager.add_command('shell',      Shell(make_context=_make_context))
manager.add_command('db_migrate', MigrateCommand)

if __name__ == '__main__':
    manager.run()