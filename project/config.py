import os

DEBUG = os.getenv('DEBUG', True)
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'mysql://hackaton:hackaton@localhost/hackaton?charset=utf8mb4')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', True)
HOST = os.getenv('HOST', 'http://liteheaven.ru:8080/')
