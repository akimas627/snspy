from flask import(
    Blueprint, render_template, request
)

from flaskr.forms import LoginForm, RegisterForm

# Blueprint＝アプリケーションをモジュールに分割できるもの。また今回はルーティングの定義にも用いる。
# view関数のグループ化にも役立つ
bp = Blueprint('app', __name__)

# トップページview
@bp.route('/')
def top():
    return render_template('top.html')

# ログインview
@bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        loginuser = LoginForm
        # DB処理を書く
        return render_template('top.html')
    return render_template('login.html', form = form)

# 登録view
@bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        # DB処理を書く
        return render_template('register.html', form = form)
    return render_template('register.html', form = form)