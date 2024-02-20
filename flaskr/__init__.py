from flask import Flask


#__init__では初期化を行うために作られている
def app_create():
    # appの定義
    app = Flask(__name__)
    
    from flaskr.views import bp
    # Blueprintの定義
    app.register_blueprint(bp)
    return app