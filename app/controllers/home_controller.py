from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app.forms.support_form import SupportForm, RespondAppeal
from app.models.support import Support
from app.models.qa import Qa
from app.forms.add_qa_form import AddQA
from datetime import datetime

@app.route('/')
@login_required
def main_page():
    return render_template('home/home.html', title='Главная')


@app.route('/support', methods=['GET','POST'])
def support_page():

    form = SupportForm()

    if form.validate_on_submit():
        support = Support(type_of_question=form.type_of_question.data,
                           question=form.question.data,
                           name=form.name.data,
                           email_for_reply=form.email_for_reply.data )
        db.session.add(support)
        db.session.commit()
        flash('Вопрос был отправлен!', 'success')
        return redirect(url_for('main_page'))
    return render_template('home/support.html', form=form)


@app.route('/support/show-appeals')
@login_required
def show_appeals():

    all_appeals = Support.query.all()
    return render_template('home/appeals_list.html', all_appeals=all_appeals)

@app.route('/support/show-appeals/<int:id>', methods=['GET','POST'])
@login_required
def show_appeal(id):
    
    appeal = Support.query.get_or_404(id)

    form = RespondAppeal()

    if form.validate_on_submit():
        appeal.respond = form.response_field.data
        appeal.date_of_respond = datetime.utcnow()
        appeal.processed_or_not = True
        
        db.session.commit()
        flash('Ответ успешно сохранен!', 'success')

        return redirect(url_for('show_appeals'))
    return render_template('home/show_appeal.html', form=form, appeal=appeal)


@app.route('/qa')
def qa_page():

    all_qa = Qa.query.all()

    return render_template('home/qa.html', all_qa=all_qa)


@app.route('/qa/add', methods=['GET', 'POST'])
@login_required
def add_qa():

    form = AddQA()

    if form.validate_on_submit():
        new_qa = Qa(question=form.new_question.data, response=form.new_answer.data)
        db.session.add(new_qa)
        db.session.commit()
        flash('Новый вопрос был успешно добавлен!', 'success')
        return redirect(url_for('qa_page'))
    return render_template('home/add_qa.html', form=form)

@app.route('/qa/change/<int:id>', methods=['GET','POST'])
@login_required
def change_qa(id):

    qa = Qa.query.get_or_404(id)

    form = AddQA()
    
    if form.validate_on_submit():
        qa.question = form.new_question.data
        qa.response = form.new_answer.data
        db.session.commit()
        flash('Вопрос и ответ были изменены успешно!', 'success')
        return redirect(url_for('qa_page'))
    form.new_question.data = qa.question
    form.new_answer.data = qa.response
    return render_template('main/add_edit_form.html', form=form, sub_title='Изменение вопроса и ответа')


@app.route('/qa/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete_qa(id):

    delete_qa = Qa.query.get_or_404(id)
    db.session.delete(delete_qa)
    db.session.commit()
    flash('Вопрос был успешно удален!', 'success')
    return redirect(url_for('qa_page'))
    


@app.route('/about')
def about_page():
    return render_template('home/about.html')

