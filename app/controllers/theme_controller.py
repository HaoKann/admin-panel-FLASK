from app import app
from flask import redirect, request, g, make_response
from app.forms.theme_form import ChangeTheme


@app.before_request
def add_theme_form():
    g.theme_form = ChangeTheme()
    # g.theme_form.chosen_theme.default = request.cookies.get('theme')
    # g.theme_form.chosen_theme.process(formdata=None)

@app.route('/change-theme', methods=['POST'])
def change_theme():
    
    if g.theme_form.validate_on_submit():
        res = make_response('Установка темы')
        res.set_cookie('theme', g.theme_form.chosen_theme.data, 30*24*60*60)
        res.headers['location'] = request.referrer or '/'    
        return res, 302
    return redirect(request.referrer or '/')