class BaseConfig(object):
    '''
    Configuration for the children config classes.
    '''
    SECRET_KEY = 'make sure to set a very secret key'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15


class DevlopmentConfig(BaseConfig):
    '''
    Dev Config
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask_user:zhanxucong123@localhost:3306/simpledu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseException):
    pass


configs = {
    'development': DevlopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
