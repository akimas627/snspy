import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'app.view'
login_manager.login_message = 'ログインしてください'
# SQLAlchemyで指定するURIのパスを設定するために絶対パスを取得する変数
# abspath()は絶対パスに変換する
# os.path.dirname(__file__)は書かれているファイル名を取得しての相対パスに変換する
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
migrate = Migrate()

#__init__では初期化を行うために作られている
def app_create():
    # appの定義
    app = Flask(__name__)
    # SQLAlchemy用の設定キー（初期化前に行う）
    app.config['SECRET_KEY'] = 'snspy'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Blueprintの定義
    from flaskr.views import bp
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app