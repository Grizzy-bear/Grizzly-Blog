# coding=utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap

from config import Config
from flask_admin import Admin,AdminIndexView
from flask_login import LoginManager
import os

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
from app.models.blog import Blog, Portfolio, Test
from app.models.discuss import Discuss

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    # config[config_name].init_app(app)
    Config.init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    # db.app = app
    # 注册蓝本
    # 增加auth蓝本
    from app.auth import auth as auth_blueprint
    # from app.auth import auth
    # from app.admin import admin as admin_blueprint

    # from auth import views

    app.register_blueprint(auth_blueprint)
    # app.register_blueprint(views.auth)
    # app.register_blueprint(admin_blueprint)
    # 附加路由和自定义的错误页面

    # 国际化
    from flask_babelex import Babel
    babel = Babel(app)


    return app