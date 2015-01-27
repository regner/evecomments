

import os


class Config(object):
    """ Default config values. """
    DEBUG = False


class DevConfig(Config):
    """ Development configuration. """
    DEBUG                   = True
    SECRET_KEY              = 'ThisIsJustTheDevKeyAndPrmesFromSomethingElseYBA*Sga78siTD&*SA%D&A*^STD&A^ISDAS'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vagrant:vagrant@localhost/evecomments'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../evecomments.db'
    EVESSO                  = dict(
        consumer_key        ='56ef03e322fd422aab074c3cc90c3d01',
        consumer_secret     ='hfYxgV1EyYlH143bZcCBoXJw64v8u8AccAIBljQ4',
        base_url            ='https://login.eveonline.com/oauth/',
        access_token_url    ='https://login.eveonline.com/oauth/token',
        access_token_method ='POST',
        authorize_url       ='https://login.eveonline.com/oauth/authorize',
    )


class C9Config(DevConfig):
    """ Development configuration for the C9 IDE """
    EVESSO                  = dict(
        consumer_key        ='7b4585e5f43842e7b19f007d671e6dd2',
        consumer_secret     ='2NXRdItCcsixZAIN86LsqJfuAORsH269mnRfSEoT',
        base_url            ='https://login.eveonline.com/oauth/',
        access_token_url    ='https://login.eveonline.com/oauth/token',
        access_token_method ='POST',
        authorize_url       ='https://login.eveonline.com/oauth/authorize',
    )