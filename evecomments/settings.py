

class Config(object):
    """ Default config values. """
    DEBUG = False


class DevConfig(Config):
    """ Production configuration. """
    DEBUG                   = True
    SECRET_KEY              = 'ThisIsJustTheDevKeyAndPrmesFromSomethingElseYBA*Sga78siTD&*SA%D&A*^STD&A^ISDAS'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vagrant:vagrant@localhost/evecomments'