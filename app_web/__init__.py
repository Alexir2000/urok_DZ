from flask import Flask
# ищем как flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# ищем как flask-bcrypt
from flask_bcrypt import Bcrypt
# ищем как flask-login
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Эту строку мы делаем когда проект лежит в корне репозитория, как обычно делаются проекты
# в нашем случае мы делаем проект не в корне, а в подпапке урока, поэтому такие танцы с бубнами.
# Строку НИЖЕ раскомментимруем, если надо
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clicker.db'

# Определяем путь к базе данных на уровень выше текущей папки
# из которой запускаем код, то-есть базу делаем не в app_web, хотя и тут можно
# в нашем случае мы делаем проект не в корне, а в подпапке урока, поэтому такие танцы с бубнами.
# basedir = os.path.abspath(os.path.dirname(__file__))
# parentdir = os.path.abspath(os.path.join(basedir, os.pardir))
# db_path = os.path.join(parentdir, 'site.db')
# # прописываем путь к базе в ключе для алхимии
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app_web import routes


