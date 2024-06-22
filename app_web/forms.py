# Ищем как flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app_web.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Имя: ', validators=[DataRequired(), Length(min=2, max=70)])
    password = PasswordField('Пароль: ', validators=[DataRequired()])
    confirm_password = PasswordField('Повтор пароля: ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует')

class LoginForm(FlaskForm):
    username = StringField('Имя: ', validators=[DataRequired()])
    password = PasswordField('Пароль: ', validators=[DataRequired()])
    submit = SubmitField('Войти')

class EditProfileForm(FlaskForm):
    username = StringField('Имя: ', validators=[DataRequired(), Length(min=2, max=70)])
    password = PasswordField('Новый пароль: ', validators=[DataRequired()])
    confirm_password = PasswordField('Повтор пароля: ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Обновить')

