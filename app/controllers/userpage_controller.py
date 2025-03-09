from app import app, db
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.forms.change_user import ChangeProfile
from werkzeug.utils import secure_filename
import os

@app.route('/userpage')
@login_required
def show_userpage():
    return render_template('main/userpage.html')


@app.route('/userpage/change_profile', methods=['GET', 'POST'])
@login_required
def change_profile():

    form = ChangeProfile()


    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        
        f = form.photo.data
        if f:
            photo_path = os.path.join(
                os.path.dirname(app.instance_path), 'app','static', 'avatars', str(current_user.id)
            )
            filename = secure_filename(f.filename)
            if current_user.photo and os.path.exists(os.path.join(photo_path, current_user.photo)):
                os.remove(os.path.join(photo_path, current_user.photo))
            os.makedirs(photo_path, exist_ok=True)
            f.save(os.path.join( photo_path, filename ))
            current_user.photo = filename
        db.session.commit()
        return redirect(url_for('show_userpage')) 
    form.name.data = current_user.name
    form.username.data = current_user.username  
    form.email.data = current_user.email
    form.phone_number.data = current_user.phone_number
    return render_template('main/add_edit_form.html', form=form, sub_title='Изменение данных пользователя')