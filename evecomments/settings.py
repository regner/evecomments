

class Config(object):
    """ Default config values. """
    DEBUG = False


class DevConfig(Config):
    """ Production configuration. """
    DEBUG                 = True
    SECRET_KEY            = 'ThisIsJustTheDevKeyAndPrmesFromSomethingElseYBA*S&DTAGDA&*Stdga78siTD&*SA%D&A*^STD&A^ISDAS'