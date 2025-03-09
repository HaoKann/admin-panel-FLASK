from app import app, db
from flask import render_template, redirect, url_for, flash, redirect
from app.models.suppliers import Supplier
from app.forms.supplier_form import SuppForm
from flask_login import login_required

@app.route('/suppliers')
def suppliers():

    all_suppliers = Supplier.query.all()
    return render_template('main/suppliers.html', all_suppliers=all_suppliers)

@app.route('/suppliers/add', methods=['GET','POST'])
def add_suppliers():

    form = SuppForm()
    
    if form.validate_on_submit():
        supplier = Supplier(sup_name=form.sup_name.data, address=form.address.data, phone_number=form.phone_number.data)
        db.session.add(supplier)
        db.session.commit()
        flash('Поставщик был успешно добавлен!', 'success')
        return redirect(url_for('suppliers'))
    return render_template('main/add_edit_form.html', form=form, sub_title='Добавление поставщика')

@app.route('/suppliers/<int:id>/edit', methods=['GET','POST'])
@login_required
def edit_suppliers(id):

    form = SuppForm()
    supplier = Supplier.query.get_or_404(id)
    if form.validate_on_submit():
        supplier.sup_name = form.sup_name.data
        supplier.address = form.address.data
        supplier.phone_number = form.phone_number.data
        db.session.commit()
        flash('Поставщик был успешно изменен!', 'success')
        return redirect(url_for('suppliers'))
    form.sup_name.data = supplier.sup_name
    form.address.data = supplier.address
    form.phone_number.data = supplier.phone_number
    return render_template('main/add_edit_form.html', form=form, sub_title='Изменение поставщика')


@app.route('/suppliers/<int:id>/delete')
@login_required
def delete_suppliers(id):

    supplier = Supplier.query.get_or_404(id)
    db.session.delete(supplier)
    db.session.commit()
    return redirect(url_for('suppliers'))


@app.route('/suppliers/<int:id>')
@login_required
def sup_details(id):

    sup_details = Supplier.query.get_or_404(id)
    return render_template('main/sup_details.html', sup_details=sup_details)