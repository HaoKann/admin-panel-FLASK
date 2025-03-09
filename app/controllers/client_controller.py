from app import app, db
from flask import render_template, redirect, url_for, flash, redirect
from flask_login import login_required
from app.forms.client_form import ClientForm
from app.models.client import Client


@app.route('/clients')
def clients():

    all_clients = Client.query.all()
    return render_template('main/clients.html', all_clients=all_clients)

@app.route('/clients/add', methods=['GET','POST'])
@login_required
def add_clients():

    form = ClientForm()

    if form.validate_on_submit():
        clients = Client(name=form.name.data, phone_number=form.phone_number.data, email=form.email.data)
        db.session.add(clients)
        db.session.commit()
        flash('Клиент был успешно добавлен!')
        return redirect(url_for('clients'))
    return render_template('main/add_edit_form.html', form=form, sub_title='Добавление клиента')


@app.route('/cilents/change/<int:id>', methods=['GET','POST'])
@login_required
def edit_client(id):

    clients = Client.query.get_or_404(id)

    form = ClientForm()

    if form.validate_on_submit():
        clients.name = form.name.data
        clients.phone_number = form.phone_number.data
        clients.email = form.email.data
        db.session.add(clients)
        db.session.commit()
        flash('Клиент был успешно изменён!', 'success')
        return redirect(url_for('clients'))
    form.name.data = clients.name
    form.phone_number.data = clients.phone_number
    form.email.data = clients.email
    return render_template('main/add_edit_form.html', form=form, sub_title='Изменение клиентов')


@app.route('/clients/<int:id>')
@login_required

def show_history(id):

    client = Client.query.get_or_404(id)
    return render_template('main/client_history.html', client=client)








@app.route('/clients/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete_client(id):    
    delete_client = Client.query.get_or_404(id)
    db.session.delete(delete_client)
    db.session.commit()
    flash('Клиент успешно удален!','success')
    return redirect(url_for('clients'))