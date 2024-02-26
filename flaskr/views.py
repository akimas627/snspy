from flask import(
    Blueprint, render_template, request, url_for, flash, redirect
)
from flaskr.model import User, PasswordResetToken
from flaskr.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user
from flaskr import db


# Blueprint＝アプリケーションをモジュールに分割できるもの。また今回はルーティングの定義にも用いる。
# view関数のグループ化にも役立つ
bp = Blueprint('app', __name__)

# トップページview
@bp.route('/')
def top():
    return render_template('top.html')

@bp.route('/logout')
def logout():
    logout_user() # logout_user関数でログアウトさせる
    return redirect(url_for('app.home'))

# ログインview
@bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.select_user_by(form.email.data)
        if user and user.is_active:
            login_user(user, remember=True)
            next = request.args.get('next')
        if not next:
            next = url_for('app.home')
            return redirect(next)
        elif not user:
            flash('存在しないユーザです')
        elif not user.is_active:
            flash('無効なユーザです。パスワードを再設定してください')
        elif not user.validate_password(form.password.data):
            flash('メールアドレスとパスワードの組み合わせが誤っています')
    return render_template('login.html', form=form)

# 登録view
@bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            username= form.username.data,
            email= form.email.data
        )
        with db.session.begin(subtransaction = True):
            token = PasswordResetToken.publish_token(user)
        db.session.commit()
        # メールに飛ばすほうがいい
        print(
            f'パスワード設定用URL: http://127.0.0.1:5000/reset_password/{token}'
        )
        flash('パスワード設定用のURLをお送りしました。ご確認ください')
        return redirect(url_for('app.login'))
    return render_template('register.html', form=form)