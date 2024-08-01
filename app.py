from flask import Flask, render_template, flash, redirect, url_for
from wtforms.form import Form
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Login imports
from flask_login import UserMixin,login_user, login_manager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt 

from flask_migrate import Migrate

#CSRF Token Generation
from flask_wtf.csrf import CSRFProtect
import os


app = Flask(__name__)


#Messaging System 
#This is used to create messages between grantee and granter
#WTF Documentation to set up CSRF Token : https://flask-wtf.readthedocs.io/en/0.15.x/csrf/
#Additional Credits to set up CSRF Token : https://stackoverflow.com/questions/34902378/where-do-i-get-secret-key-for-flask
app.config['SECRET_KEY'] = os.urandom(24).hex()

#Database
#had to use full path due to use of OneDrive. Will need to correct this later on for Heroku.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/PhilDoopeeDoo/OneDrive - DPD/M3Project/M3Project/data/m3project.db'
db = SQLAlchemy(app) 
bcrypt = Bcrypt(app)

#Flask-Migrate documentation 
migrate = Migrate(app, db)

#CSRF Token
csrf = CSRFProtect(app) 

#Models
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password= db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    company_name = db.Column(db.String(200), unique=True, nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


#Forms
class UserRegisterForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Username"})
    email_address = StringField("Enter your email address", validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Email Address"})
    password = PasswordField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Password"})
    company_name = StringField("Enter your company name", validators=[Length(max=200)], render_kw={"placeholder": "Company Name"})
    submit = SubmitField("Register")

    #checks if username already exists: credit to Arpan Neupane's tutorial on Youtube
    def validate_username(self,username):
        existing_user_username = User.query.filter_by(username=username.data).first()

        if existing_user_username:
            raise ValidationError("This username is already used")

class UserLoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Username"})
    email_address = StringField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Email Address"})
    password = PasswordField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")
    
class MessagingForm(FlaskForm):
    #TODO: automatically add username without user input later on
    username = StringField("Enter username", validators=[DataRequired(),])
    #TODO: if message is related to specific grant ID, add logic to pass ID field
    message = StringField("Provide message", validators=[DataRequired()])
    submit = SubmitField('Submit')


# Authentication logic
#Index page is login page
@app.route("/", methods=["GET","POST"])
def index():
    form = UserLoginForm()
    users = User.query.all()

    return render_template('index.html', form=form, users=users)

#register page
@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(
            username=form.username.data, 
            password=hashed_password,
            email=form.email_address.data, 
            company_name=form.company_name.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created', 'success')
        return redirect(url_for('index'))
    else:
        flash('Account not created', 'danger')
        print("The form didnt get created")
    return render_template('register.html', form=form)


# Error Page Handling
@app.errorhandler(404)
def page_not_found_error(e):
   
    return render_template('error-handling/404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error-handling/500.html')

# User Interface logic

#dashboard
@app.route("/dashboard")
def dashboard():
    return render_template('grantee/grantee-dashboard.html')

#displays grants available
@app.route("/grants-available")
def grant_available():
    return render_template('grantee/grants-available.html')

#interface to manage grants allocated to user account
@app.route("/manage-grants")
def manage_grant():
    return render_template('grantee/manage-grants.html')

#interface to edit or delete to user account
@app.route("/account")
def account():
    return render_template('grantee/account.html')

#Allows user to contact granter for any question
#PROBLEM : `'MessagingForm' object has no attribute 'validate_on_submit'` this is because I imported the wrong form. 
#Official documentation created this error
#SOlution credits: https://stackoverflow.com/questions/22873794/attributeerror-editform-object-has-no-attribute-validate-on-submit
@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    username = None
    message = None
    form = MessagingForm()
    
    if form.validate_on_submit():
        username = form.username.data
        message = form.message.data
        form.username.data = ''
        form.message.data = ''
        print('The form has been submited')
        flash('Message is sent')
    return render_template('grantee/contact-us.html',
        username = username,
        message = message,
        form = form)

# Granter Interface Logic

if __name__ == "__main__":
    app.run(debug=True)
