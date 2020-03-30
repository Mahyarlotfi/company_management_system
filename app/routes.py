from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import LoginForm, RegisterNewProjectForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Project, Income_Expense


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/submitnewproject', methods=['GET', 'POST'])
@login_required
def submitnewproject():
    Project_Table = Project.query.all()
    form = RegisterNewProjectForm()
    if form.validate_on_submit():
        NEW_PROJECT = Project(project_name=form.project_name.data,
                              investment_type=form.investment_type.data,
                              company_share=form.company_share.data,
                              non_corporated_partners=form.non_corporated_partners.data,
                              start_date=form.start_date.data,
                              end_date=form.end_date.data,
                              description=form.description.data)
        db.session.add(NEW_PROJECT)
        db.session.commit()
    for i in Project_Table:
        print (i)
    return render_template('submitnewproject.html', form=form, data=Project_Table)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
