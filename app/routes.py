from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('login.html'))
    return render_template('login.html', form=form)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello'
