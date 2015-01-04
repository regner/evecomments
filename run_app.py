

import os

from flask.ext.script  import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

from evecomments.app        import create_app
from evecomments.settings   import DevConfig, C9Config
from evecomments.extensions import db

if os.environ.get('EI_ENV') == 'prod':
    pass
    #app = create_app(ProdConfig)

elif os.environ.get('EI_ENV') == 'c9':
    app    = create_app(C9Config)
    server = Server(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

else:
    app    = create_app(DevConfig)
    server = Server()


migrate = Migrate(app, db)
manager = Manager(app)


def _make_context():
    """ Return context dict for a shell session so you can access. """

    return {'app': app, 'db': db}


manager.add_command('server',     server)
manager.add_command('shell',      Shell(make_context=_make_context))
manager.add_command('db_migrate', MigrateCommand)

if __name__ == '__main__':
    manager.run()