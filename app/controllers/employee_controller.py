from app import app, db
from flask import render_template, redirect, url_for, flash, redirect
from flask_login import login_required
from app.forms.employee_form import EmployeeForm
from app.models.employees import Employee



@app.route('/employee')
def employee():

    all_employees = Employee.query.all()
    return render_template('main/employees.html', all_employees=all_employees)

@app.route('/employee/add', methods=['GET','POST'])
def add_employee():

    form = EmployeeForm()

    if form.validate_on_submit():
        employees = Employee(name=form.name.data, surname=form.surname.data, date_of_birth=form.date_of_birth.data, address=form.address.data, salary=form.salary.data)
        db.session.add(employees)
        db.session.commit()
        flash('Работник был успешно добавлен!')
        return redirect(url_for('employee'))
    return render_template('main/add_edit_form.html', form=form, sub_title='Добавление сотрудника' )

@app.route('/employee/change/<int:id>', methods=['GET','POST'])
@login_required
def change_employee(id):

    employee = Employee.query.get_or_404(id)

    form = EmployeeForm()

    if form.validate_on_submit():
        employee.name = form.name.data
        employee.surname = form.surname.data
        employee.date_of_birth = form.date_of_birth.data
        employee.address = form.address.data
        employee.salary = form.salary.data
        db.session.add(employee)
        db.session.commit()
        flash('Сотрудник успешно изменён!', 'success')
        return redirect(url_for('employee'))
    form.name.data = employee.name
    form.surname.data = employee.surname
    form.date_of_birth.data = employee.date_of_birth
    form.address.data = employee.address
    form.salary.data = employee.salary
    return render_template('main/add_edit_form.html', form=form, sub_title='Изменение сотрудника')



@app.route('/delete/employee/<int:id>', methods=['GET','POST'])
@login_required
def delete_employee(id):

    employee_delete = Employee.query.get_or_404(id)
    db.session.delete(employee_delete)
    db.session.commit()
    flash('Сотрудник успешно удален!', 'success')
    return redirect(url_for('employee'))