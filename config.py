import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MAX_NUMBER_OF_VOTERS = 5
    MAX_NUMBER_OF_CANDIDATES = 3
    ALLOW_VOTING = False
    PUBLISH_RESULTS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
