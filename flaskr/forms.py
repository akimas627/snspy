from wtforms.form import Form
from wtforms.fields import (
    StringField, PasswordField,  SubmitField
)
from wtforms.validators import (
    DataRequired, Email, EqualTo,
)
from wtforms import ValidationError
from flaskr.model import User

# ログイン用のフォーム
class LoginForm(Form):
    email = StringField('メールアドレス: ', validators=[DataRequired(), Email('これメールアドレスじゃないです')])
    password = PasswordField(
        'パスワード: ', validators=[DataRequired(),EqualTo('confirm_password', message='パスワードが違います')]
        )
    confirm_password = PasswordField('パスワードを再入力してください: ', validators=[DataRequired()])
    submit = SubmitField('送信')

# 登録用のフォーム
class RegisterForm(Form):
    username = StringField('お名前: ', validators=[DataRequired()])
    email = StringField('メールアドレス: ', validators=[DataRequired(), Email('これメールアドレスじゃないです')])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_user_by_email(field.data):
            raise ValidationError('メールアドレスはすでに登録されています')
