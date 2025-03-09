from app import app, db
from flask import render_template, redirect, url_for, flash, redirect
from app.forms.orders_form import OrderForm
from app.models.orders import Order, ProductInCart
from flask_login import login_required
from app.models.client import Client
from app.forms.product_in_cart_form import AddProductInCart
from app.models.product import Product
from app.forms.confirm_form import ConfirmForm

@app.route('/orders')
def orders():

    all_orders = Order.query.all()
    return render_template('main/orders.html', all_orders=all_orders)

@app.route('/order/add', methods=['GET','POST'])
@login_required
def add_order():

    form = OrderForm()

    all_clients = db.session.query(Client).order_by(Client.name, Client.phone_number).all()
    
    form.client_id.choices=[(client.id, f'{client.name} ({client.phone_number}, {client.email})') for client in all_clients]

    if form.validate_on_submit():
        orders = Order(order_description=form.order_description.data, date=form.date.data, client_id=form.client_id.data)
        db.session.add(orders)
        db.session.commit()
        flash('Заказ был успешно добавлен!')
        return redirect(url_for('orders'))
    return render_template('main/add_edit_form.html', form=form, sub_title='Добавление заказ')


@app.route('/order/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_order(id):

    order_change = Order.query.get_or_404(id)

    form = OrderForm()

    form.client_id.choices= [(client.id, client.name) for client in Client.query.all()]

    if form.validate_on_submit():
        order_change.order_description = form.order_description.data
        order_change.date = form.date.data
        order_change.client_id = form.client_id.data
        db.session.add(order_change)
        db.session.commit()
        flash('Заказ успешно изменен!', 'success')
        return redirect(url_for('orders'))
    form.order_description.data =  order_change.order_description
    form.date.data = order_change.date
    form.client_id.data = order_change.client_id
    return render_template('main/add_edit_form.html', form=form, sub_title='Изменение заказа')

@app.route('/order/delete/<int:id>')
def delete_order(id):
    
    order_id = Order.query.get_or_404(id)
    db.session.delete(order_id)
    db.session.commit()
    flash('Заказ был успешно удален!', 'sucess')
    return redirect(url_for('orders'))



@app.route('/order/<int:id>', methods=['GET','POST'])
def order_details(id):

    order = Order.query.get_or_404(id)

    
    products_in_cart = [product_in_cart.product.id for product_in_cart in order.products.all()]


    form = AddProductInCart()

    form.product.choices = [(product.id, product.prod_name)  for product in Product.query.all() if product.id not in products_in_cart]

    # all_products = []
    # for product in Product.query.all():
        

    if form.validate_on_submit():
        prod_in_cart = ProductInCart(amount=form.amount.data, order_id=id, product_id=form.product.data)
        db.session.add(prod_in_cart)
        db.session.commit()
        flash('Товар был добавлен в корзину!', 'success')
        return redirect(url_for('order_details', id=id))
    return render_template('main/order_details.html', form=form, order=order)



@app.route('/order-details/change/<int:id>', methods=['GET','POST'])
def change_product_in_cart(id):

    prod_in_cart = ProductInCart.query.get_or_404(id)


    products_in_cart = [product_in_cart.product.id for product_in_cart in prod_in_cart.order.products.all() if product_in_cart.id != prod_in_cart.id ]

    form = AddProductInCart()

    form.product.choices = [(product.id, product.prod_name) for product in Product.query.all() if product.id not in products_in_cart]

    if form.validate_on_submit():
        prod_in_cart.product_id = form.product.data
        prod_in_cart.amount = form.amount.data
        db.session.commit()
        flash('Детали заказа были изменены успешно!','success')
        return redirect(url_for('order_details', id=prod_in_cart.order_id))
    form.product.data = prod_in_cart.product_id
    form.amount.data = prod_in_cart.amount
    return render_template('main/add_edit_form.html', form=form, sub_title='Изменение деталей заказа')
   

@app.route('/order-details/delete/<int:id>', methods=['GET','POST'])
def delete_product_in_cart(id):

    form = ConfirmForm()

    if form.validate_on_submit():
        delete_order_details = ProductInCart.query.get_or_404(id)
        db.session.delete(delete_order_details)
        db.session.commit()
        flash('Продукт из корзины был удален успешно!', 'success')
        return redirect(url_for('order_details', id=delete_order_details.order_id))
    return render_template('main/add_edit_form.html', form=form, sub_title='Вы точно хотите удалить товар из заказа?')