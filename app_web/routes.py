from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app_web.models import User
from app_web import app, db, bcrypt
from app_web.forms import RegistrationForm, LoginForm, EditProfileForm

@app.route('/')
@login_required
def index():
    return render_template('index.html', title='Главная')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляем! Вы зарегистрировались!', 'Успешно!')
        """
        В Flask, вы можете использовать любую строку в качестве категории 
        при вызове функции `flash`. Нет зарезервированных категорий,
         и вы можете создавать свои собственные категории, 
         чтобы лучше организовать и отобразить сообщения.
                Тем не менее, существуют некоторые общие практики и соглашения, 
            которые часто используются для улучшения читаемости и поддержки кода. 
            пример, часто используются категории, такие как 
            `success`, `error`, `warning`, `info`, и т.д., 
            чтобы соответствовать различным уровням уведомлений.
            flash('Введены неверные данные', 'error')
            flash('Регистрация прошла успешно', 'success')
        """
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Регистрация')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember="False") # Параметр remember - задает куки для запоминания юзера
            return redirect(url_for('index'))
        else:
            flash('Введены неверные данные', 'Ошибка!')
    return render_template('login.html', form=form, title='Страница входа')


@app.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', 'Успешно!')
    return redirect(url_for('index'),)



@app.route('/click')
@login_required
def click():
    current_user.clicks += 1
    db.session.commit()
    return render_template('index.html', title='Главная')

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.username = form.username.data
        if form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            current_user.password = hashed_password
        db.session.commit()
        flash('Ваши изменения сохранены.', 'Успешно!')
        return redirect(url_for('index'), title='Главная')
    return render_template('edit_profile.html', form=form, title='Редактирование профиля')

