import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', default='wE1lpO$ivbY4luRO')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', default='sqlite:///' + os.path.join(basedir, 'database.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', default=False)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', default='smtp.qq.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', default=465)
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', default=True)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', default=False)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', default='diostudio@foxmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', default='lasgikitgydubjaa')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', default=('DIOSTUDIO', 'diostudio@foxmail.com'))
    MAIL_SUBJECT_PREFIX = os.environ.get('MAIL_SUBJECT_PREFIX', default='[DIOSTUDIO]')
    MAIL_SENDER = os.environ.get('MAIL_SENDER', default='DIOSTUDIO <diostudio@foxmail.com>')
    pass
