import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(basedir, '..', 'post_nlp.db')
TITLE = "Играем с FastAI"
LIMIT_COUNT = 5
