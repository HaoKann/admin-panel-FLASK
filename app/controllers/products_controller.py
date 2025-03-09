from app.models.product import Product
from app import app, db
from flask import render_template, redirect, url_for, flash, redirect
from flask_login import login_required
from app.models.suppliers import Supplier
from app.forms.product_form import ProdForm
from app.forms.confirm_form import ConfirmForm

@app.route('/products')
def products():

    all_products = Product.query.all()
    return render_template('main/products.html', all_products=all_products)

@app.route('/products/add', methods=['GET','POST'])
@login_required
def add_products():

    form = ProdForm()

    form.supplier_id.choices =[(sup.id, sup.sup_name) for sup in Supplier.query.all()]

    if form.validate_on_submit():
        products = Product(prod_name=form.prod_name.data, suppliers_id=form.supplier_id.data ,prod_type=form.prod_type.data, prod_amount=form.prod_amount.data, prod_price=form.prod_price.data)
        db.session.add(products)
        db.session.commit()
        flash('Продукт был успешно добавлен!', 'success')
        return redirect(url_for('products'))
    return render_template('main/add_edit_form.html', form=form, sub_title='Добавление товара')


@app.route('/products/change/<int:id>', methods=['GET','POST'])
@login_required
def change_product(id):
    
    products = Product.query.get_or_404(id)

    form = ProdForm()

    form.supplier_id.choices =[(sup.id, sup.sup_name) for sup in Supplier.query.all()]

    if form.validate_on_submit():
        products.prod_name = form.prod_name.data
        products.prod_type = form.prod_type.data
        products.suppliers_id = form.supplier_id.data
        products.prod_amount = form.prod_amount.data
        products.prod_price = form.prod_price.data
        db.session.add(products)
        db.session.commit()
        flash('Продукт был успешно изменен!', 'sucess')
        return redirect(url_for('products'))
    form.prod_name.data = products.prod_name
    form.prod_type.data = products.prod_type
    form.supplier_id.data = products.suppliers_id
    form.prod_amount.data = products.prod_amount
    form.prod_price.data =  products.prod_price
    return render_template('main/add_edit_form.html', form=form, sub_title='Изменение товара')

@app.route('/products/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete_product(id):
    delete_products = Product.query.get_or_404(id)

    form = ConfirmForm()

    if form.validate_on_submit():
        db.session.delete(delete_products)
        db.session.commit()
        flash('Продукт был удален')
        return redirect(url_for('products'))
    return render_template('main/add_edit_form.html', form=form, sub_title = f'Вы точно хотите удалить продукт "{delete_products.prod_name}"?')
