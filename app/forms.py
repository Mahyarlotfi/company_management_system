'''Create All form in this file'''
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     PasswordField,
                     BooleanField,
                     SubmitField,
                     DateField,
                     SelectField,
                     IntegerField)
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    '''Login Form for website'''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterNewProjectForm(FlaskForm):
    '''form for registering new progect'''
    project_name = StringField('Project Name', validators=[DataRequired()])
    investment_type = SelectField('Investment Type', validators=[DataRequired()], choices=[('1', 'Buy Land'), ('2', 'House Reconstruction')])
    company_share = IntegerField('Company Share')
    non_corporated_partners = StringField('Non Corporated Partners')
    start_date = DateField('Start Date')
    end_date = DateField('End Date')
    description = StringField('Description')
    submit = SubmitField('Register')
