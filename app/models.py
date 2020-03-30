from app import db
from werkzeug.security import (generate_password_hash
                               , check_password_hash)
from flask_login import UserMixin
from app import login
import jdatetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    first_name = db.Column(db.String(16), index=True)
    last_name = db.Column(db.String(16), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    position =  db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    income_expense = db.relationship('Income_Expense', backref='spender', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.first_name}', '{self.last_name}', '{self.email}', '{self.position}')"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    project_name = db.Column(db.String(32), index=True, unique=True) 
    investment_type = db.Column(db.String(32), index=True)
    company_share = db.Column(db.Integer, index=True)
    non_corporated_partners = db.Column(db.String(128), index=True)
    start_date = db.Column(db.DateTime, index=True)
    end_date = db.Column(db.DateTime, index=True)
    description = db.Column(db.String(256), index=True)
    income_expense = db.relationship('Income_Expense', backref='project_finance', lazy=True)

    def __repr__(self):
        return f"Project('{self.project_name}', '{self.investment_type}', '{self.company_share}', '{self.start_date}', '{self.start_date}', '{self.description}')"


class Income_Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost_type = db.Column(db.String(32), index=True)
    payment_method = db.Column(db.String(32), index=True)
    date_of_payment = db.Column(db.DateTime, index=True, unique=True)
    amount = db.Column(db.BigInteger, index=True)
    description = db.Column(db.String(256), index=True)
    image = db.Column(db.String(20), index=True)
    date_of_submit = db.Column(db.DateTime, index=True, unique=True, default=jdatetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False) 

    def __repr__(self):
        return f"Income_Expense('{self.cost_type}', '{self.payment_method}', '{self.date_of_payment}', '{self.amount}', '{self.description}, '{self.date_of_submit}')"



@login.user_loader
def load_user(id):
    return User.query.get(int(id))
