from flask import Flask, render_template, flash, redirect, url_for
from wtforms.form import Form
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Login imports
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt, check_password_hash

from flask_migrate import Migrate

#CSRF Token Generation
from flask_wtf.csrf import CSRFProtect
import os

#enumaration (used to pre-define user types)
import enum


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

#Flask-Login
#documentation: https://flask-login.readthedocs.io/en/latest/
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "index"
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#CSRF Token
csrf = CSRFProtect(app) 



#Models

class UserType(enum.Enum):
    GRANTEE = "Grantee"
    GRANTER = "Granter"

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password= db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    company_name = db.Column(db.String(200), unique=True, nullable=True)
    user_type = db.Column(db.Enum(UserType), nullable=False, default=UserType.GRANTEE)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username} {self.email} {self.company_name}>'

class Grant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grant_title = db.Column(db.String(200), unique=True, nullable=False)
    grant_description = db.Column(db.String(200), unique=True, nullable=False)
    grant_fund = db.Column(db.Integer, nullable=False, default=0)
    created_on = created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.grant_title} {self.grant_description} {self.grant_fund}>'

#Forms
class UserRegisterForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Username"})
    email_address = StringField("Enter your email address", validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Email Address"})
    password = PasswordField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Password"})
    company_name = StringField("Enter your company name", validators=[Length(max=200)], render_kw={"placeholder": "Company Name"})
    user_type = SelectField("Select User Type", choices=[(UserType.GRANTEE.value, "Grantee"), (UserType.GRANTER.value, "Granter")], validators=[DataRequired()])
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

class AddGrantForm(FlaskForm):
    grant_title = StringField("Enter Grant Title", validators=[DataRequired(),])
    grant_description = StringField("Enter Grant Description", validators=[DataRequired(),])
    grant_fund = IntegerField("Enter Fund Value", validators=[DataRequired(),])
    submit = SubmitField('Submit')

#Functions

#Admin Panel
@app.route("/admin", methods=["GET","POST"])
# @login_required
def admin():
    #list users
    #list grants
    grants = Grant.query.all()
    print(grants)

    #form to add grants
    grantform = AddGrantForm()
    if grantform.validate_on_submit():
        newgrant = Grant(
            grant_title = grantform.grant_title.data,
            grant_description = grantform.grant_description.data,
            grant_fund = grantform.grant_fund.data
        )
        db.session.add(newgrant)
        db.session.commit()
        flash('Grant has been added', 'success')
        return redirect(url_for('admin'))
    else:
        print("the form is not valid")

    #create for loop to list all grants available
    for grant in grants:
        print(grant)
        


    return render_template('admin/admin.html', grants=grants, grantform=grantform)

# Authentication logic
#Index page is login page
@app.route("/", methods=["GET","POST"])
def index():
    form = UserLoginForm()
    users = User.query.all()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        print("the user is")
        #if user exist confirm password
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash("The password does not exist")
                print("The password does not exist")
        else:
            flash("The user does not exist")
            print("The user does not exist")

    #form to add grants


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
            company_name=form.company_name.data,
            user_type=UserType(form.user_type.data)
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created', 'success')
        login_user(new_user)
        return redirect(url_for('dashboard'))
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
@login_required
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

#Show grant_id content
@app.route('/show_grant/<int:grant_id>', methods=['GET'])
def show_grant(grant_id):
    grant = Grant.query.get_or_404(grant_id)
    return render_template('granter/show_grant.html')


if __name__ == "__main__":
    app.run(debug=True)
