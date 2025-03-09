from app import app, db

from flask import render_template, redirect, url_for, flash, redirect, request

from app.forms.login_form import LoginForm
from app.forms.registration_form import RegForm

from flask_login import current_user, login_required, logout_user, login_user

from urllib.parse import urlparse

from app.forms.change_password import ChangePassword
from app.models.user import User

@app.route('/reg', methods=['GET','POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    
    form = RegForm()

    if form.validate_on_submit():
        reg_user = User(name=form.name.data, username=form.username.data, email=form.email.data, phone_number=form.phone_number.data)
        reg_user.set_password(form.password1.data)
        db.session.add(reg_user)
        db.session.commit()
        flash('Аккаунт создан успешно', 'success')
        return redirect(url_for('login'))
    return render_template('auth/reg.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('main_page')
            flash('Вход выполнен успешно', 'success')
            return redirect(next_page)
        
        flash('Неверный логин или пароль','danger')
        return redirect(url_for('login'))
    return render_template('auth/login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы','info')
    return redirect(url_for('login'))


@app.route('/userpage/changepassword', methods=['GET','POST'])
@login_required
def change_password():
    form = ChangePassword()

    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.new_password1.data)
            db.session.commit()
            flash('Пароль изменён успешно!', 'success')
            return redirect(url_for('main_page'))
        else:
            flash('Пароль не был изменён, попробуйте заново', 'danger')
            return redirect(url_for('change_password'))
        
    return render_template('main/change_password.html', form=form)


