from flask import Flask, render_template, flash, redirect, url_for, request
from wtforms.form import Form
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError,Regexp
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
#Allows for environment variables
from dotenv import load_dotenv

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
# app.config['SECRET_KEY'] = os.urandom(24).hex()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_dev_key')

#Database
#had to use full path due to use of OneDrive. Will need to correct this later on for Heroku.
load_dotenv()  # take environment variables from .env.

#Fix for heroku database noted as postgres intsead of postgresql
#Credit: https://stackoverflow.com/questions/66690321/flask-and-heroku-sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url

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
    company_name = db.Column(db.String(200), nullable=True)
    user_type = db.Column(db.Enum(UserType), nullable=False, default=UserType.GRANTEE)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __repr__(self):
        return f'<{self.username} {self.email} {self.company_name}>'

class Grant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='usergrants')
    grant_title = db.Column(db.String(200), unique=True, nullable=False)
    grant_description = db.Column(db.String(200), nullable=False)
    grant_fund = db.Column(db.Integer, nullable=False, default=0)
    created_on = created_on = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=False)
    is_closed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<{self.grant_title} {self.grant_description} {self.grant_fund}>'

class GrantQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='usergrantquestions')
    grant_id = db.Column(db.Integer, db.ForeignKey('grant.id'))
    grant = db.relationship('Grant', backref='questions')
    question = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    answers = db.relationship('GrantAnswer', back_populates='grant_question', lazy=True)

    def __repr__(self):
        return f'<Grant: {self.grant} {self.question}>'

class GrantApplication(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='usergrantapplications')
    grant_id = db.Column(db.Integer, db.ForeignKey('grant.id'))
    grant = db.relationship('Grant', backref='applications')
    is_submitted = db.Column(db.Boolean, default=False)
    is_approved = db.Column(db.Boolean, default=False)
    is_rejected = db.Column(db.Boolean, default=False)

    answers = db.relationship('GrantAnswer', backref='grant_application', cascade='all, delete-orphan')
    def __repr__(self):
        return f'<GrantApplication: {self.user_id} {self.grant_id}>'



class GrantAnswer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='usergrantanswers')
    application_id = db.Column(db.Integer, db.ForeignKey('grant_application.id'))
    application = db.relationship('GrantApplication', backref='userapplications')
    grant_question_id = db.Column(db.Integer, db.ForeignKey('grant_question.id'))#the FK was automatically named `grant_question` in the migration.
    grant_question = db.relationship('GrantQuestion', back_populates='answers')
    answer = db.Column(db.String(300), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)



    def __repr__(self):
         return f'<GrantAnswer: {self.grant_question} {self.answer}>'

#Forms

class UserRegisterForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Username"})
    email_address = StringField("Enter your email address", validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Email Address"})
    
    password = PasswordField(
        "Enter your password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least 8 characters long."),
            Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+=-]{8,}$', message="Password must contain at least one letter, one number. You can also include special characters.")
        ],
        render_kw={"placeholder": "Password"}
    )
    
    confirm_password = PasswordField(
        "Confirm your password",
        validators=[
            DataRequired(),
            Length(min=8),
            Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+=-]{8,}$')
        ],
        render_kw={"placeholder": "Confirm Password"}
    )
    
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("This username is already used")

class UserLoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")
   
class MessagingForm(FlaskForm):
    #TODO: automatically add username without user input later on
    username = StringField("Enter username", validators=[DataRequired(),])
    #TODO: if message is related to specific grant ID, add logic to pass ID field
    message = StringField("Provide message", validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddGrantForm(FlaskForm):
    grant_title = TextAreaField("Enter Grant Title", validators=[DataRequired(), Length(max=200)], render_kw={"maxlength": 200, "class": "form-control", "placeholder": "Enter Grant Title", "rows": 1})
    grant_description = TextAreaField("Enter Grant Description", validators=[DataRequired(), Length(max=200)], render_kw={"maxlength": 200, "class": "form-control", "placeholder": "Enter Description", "rows": 3})
    grant_fund = IntegerField("Enter Fund Value", validators=[DataRequired()], render_kw={"class": "form-control", "placeholder": "Enter Grant Value"})
    submit = SubmitField('Submit')

class AddGrantQuestionForm(FlaskForm):
    question = TextAreaField("Enter Question", validators=[DataRequired(),Length(max=200)], render_kw={"maxlength": 200, "class": "form-control", "placeholder": "Enter Grant Title", "rows": 3})
    submit = SubmitField('Submit')

class EditGrantQuestionForm(FlaskForm):
    question = TextAreaField("Enter Question", validators=[DataRequired(),Length(max=200)], render_kw={"maxlength": 200, "class": "form-control", "placeholder": "Enter Grant Title", "rows": 3})
    submit = SubmitField('Submit')

class AnswerGrantQuestionForm(FlaskForm):
    answer = StringField("Enter Answer", validators=[DataRequired(),])
    submit = SubmitField('Submit')
#Functions

@app.context_processor
def inject_user_type():
    return dict(UserType=UserType)

#allows to display intergers in models as currency
@app.template_filter('currency')
def currency_filter(value):
    try:
        return f"£ {value:,.2f}"
    except (ValueError, TypeError):
        return value

#Admin Panel
@app.route("/admin", methods=["GET","POST"])
@login_required
def admin():
    #list users
    users = User.query.order_by(User.id).all()
    #list grants
    grants = Grant.query.all()
    print(grants)

    return render_template('admin/admin.html', 
    grants=grants, 
    users=users)

@login_required
@app.route("/change-user-status/<int:user_id>", methods=["GET", "POST"])
def change_user_status(user_id):
    selected_user = User.query.get_or_404(user_id)
    print(f"selected_user = {selected_user}")
    if selected_user.user_type == UserType.GRANTEE:
        selected_user.user_type = UserType.GRANTER
    else:
        selected_user.user_type = UserType.GRANTEE
        
    db.session.commit()
    return redirect(url_for("admin"))


#Authentication logic
#Index page is login page
@app.route("/", methods=["GET","POST"])
def index():
    #if user is authenticated
    #Redirect based on the user type
    if current_user.is_authenticated:      
            if current_user.user_type == UserType.GRANTER:
                return redirect(url_for('granter_dashboard'))
            elif current_user.user_type == UserType.GRANTEE:
                return redirect(url_for('dashboard'))

    form = UserLoginForm()
   
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        #if user exist confirm password
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                if current_user.user_type != UserType.GRANTER:
                    return redirect(url_for('dashboard'))
                else:
                    return redirect(url_for('granter_dashboard'))
            else:
                flash("The password does not exist")
                print("The password does not exist")
        else:
            flash("The user does not exist")
            print("The user does not exist")

    return render_template('index.html', form=form)

#register page
@app.route("/register", methods=["GET", "POST"])
def register():
    #if user is authenticated
    #Redirect based on the user type
    if current_user.is_authenticated:      
        if current_user.user_type == UserType.GRANTER:
            return redirect(url_for('granter_dashboard'))
        elif current_user.user_type == UserType.GRANTEE:
            return redirect(url_for('dashboard'))

    form = UserRegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        existing_email = User.query.filter_by(email=form.email_address.data).first()

        if existing_user:
            flash('Username already exists.', 'danger')
            return render_template('register.html', form=form)

        if existing_email:
            flash('Email address already in use.', 'danger')
            return render_template('register.html', form=form)

        # Print the plaintext password to console (only for development, not for production)
        print(f'Plaintext password = {form.password.data}')
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print(f'Hashed password = {hashed_password}')
        new_user = User(
            username=form.username.data, 
            password=hashed_password,
            email=form.email_address.data, 
        )
      
        db.session.add(new_user)
        db.session.commit()
        flash('Account created', 'success')
        login_user(new_user)
        if current_user.user_type != UserType.GRANTER:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('granter_dashboard'))

    else:
        print(f"Form validation errors: {form.errors}")  # Print form validation errors
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

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
    applications = GrantApplication.query.filter_by(user_id = current_user.id).order_by(GrantApplication.id).all()
    print(f'applications = {applications}')
    
    return render_template('grantee/grantee-dashboard.html',
    applications=applications)

#displays grants available

@app.route("/grants-available")
@login_required
def grant_available():
    grants = Grant.query.filter_by(is_active=True)
    existing_applications = GrantApplication.query.filter_by(user_id=current_user.id).all()

    # search if user has already created an application (look up for existing id)
    #same process as apply_to_grant()
    existing_application_id = {app.grant_id: app for app in existing_applications}

    return render_template('grantee/grants-available.html',
        grants=grants,
        existing_application_id=existing_application_id)

#activate application
@app.route("/activate-application/<int:grant_id>", methods=['GET', 'POST'])
@login_required
def activate_application(grant_id):

    #check if there is already an application
    existing_application = GrantApplication.query.filter_by(
        user_id=current_user.id,
        grant_id=grant_id
    ).first()
    print("existing_application is {existing_application}")

    if existing_application:
        print("user already has application. redirect to url")
        return redirect(url_for('apply_to_grant', grant_id=grant_id, grant_application_id=existing_application.id))

    #add application object
    new_application = GrantApplication(
        user_id = current_user.id,
        grant_id = grant_id
    )

    db.session.add(new_application)
    db.session.commit()

    print(f"application is created with: {new_application.id}")

    return redirect(url_for('apply_to_grant', grant_id=grant_id,grant_application_id=new_application.id))

#submit application
@app.route("/submit-application/<int:grant_id>/<int:grant_application_id>",methods=['GET', 'POST'])
@login_required
def submit_application(grant_application_id, grant_id):
    submitted_application_id = grant_application_id
    grant_id=grant_id
    print(f"submitted_application_id {submitted_application_id}")
    application = GrantApplication.query.get_or_404(grant_application_id)
    submitted_application_user_id = application.user_id
    print(f"submitted_application_user_id {submitted_application_user_id}")

    #call form

    #check to make sure no other user submits someone else's application
    if submitted_application_user_id == current_user.id:
        application.is_submitted = True

    db.session.commit()
    flash('Application submitted', 'success')

    return redirect(url_for('read_submitted_application', grant_id=grant_id,grant_application_id=grant_application_id))

#delete application
@app.route("/delete-application/<int:grant_id>/<int:grant_application_id>",methods=['POST'])
@login_required
def delete_application(grant_id,grant_application_id):

    grantapplication = GrantApplication.query.get_or_404(grant_application_id)
    db.session.delete(grantapplication)
    db.session.commit()
    flash('Application deleted')
    return redirect(request.referrer or url_for('grant_available'))

#display application after submission
@app.route("/read-submitted-application//<int:grant_id>/<int:grant_application_id>")
@login_required
def read_submitted_application(grant_id, grant_application_id):
    user_submitted_application = GrantApplication.query.get_or_404(grant_application_id)
    grant_question = GrantQuestion.query.filter(GrantQuestion.grant_id == grant_id).order_by(GrantQuestion.id).all()

    #create list to match questions and answers
    grant_question_user_answer = []

    for grantquestion in grant_question:
        user_answer = GrantAnswer.query.filter_by(grant_question_id=grantquestion.id, user_id=current_user.id).all()
        grant_question_user_answer.append({
            'question':grantquestion.question,
            'answer':[answer.answer for answer in user_answer]
        })
  
    return render_template('grantee/read-submitted-application.html',
    user_submitted_application=user_submitted_application,
    grant_question_user_answer=grant_question_user_answer,
    grant_id=grant_id,
    grant_application_id=grant_application_id
    )


#allows to apply and answer grant question
@app.route("/apply-to-grant/<int:grant_id>/<int:grant_application_id>", methods=['GET', 'POST'])
@login_required
def apply_to_grant(grant_id,grant_application_id):
    #TO DO: add logic to prvent user getting back to this page if grant is submitted
    #if appliction is submitted = redirect user to grants available page.

    grant = Grant.query.get_or_404(grant_id)
    grant_application_id = grant_application_id
    grant_application = GrantApplication.query.get_or_404(grant_application_id)
    grant_questions = GrantQuestion.query.filter_by(grant_id=grant_id).order_by(GrantQuestion.id).all()
    answers = GrantAnswer.query.join(GrantQuestion).filter(
        GrantQuestion.grant_id == grant_id,
        GrantAnswer.user_id == current_user.id
    ).all()

    answers_from_user_id = {answer.grant_question_id: answer for answer in answers}
    print(answers_from_user_id)

    for grantanswer in answers:
        print(f'grantanswer.answer: {grantanswer.answer} + grantanswer.grant_question_id:{grantanswer.grant_question_id} + grantanswer.user_id: {grantanswer.user_id} ')


    editanswerform = AnswerGrantQuestionForm() # defines editanswerform in main template
    grantanswerform = AnswerGrantQuestionForm()
    if request.method == 'POST':
        grant_question_id = request.form.get('grant_question_id')
        grant_application_id = request.form.get('grant_application_id')
        #answer_form = None
        if grantanswerform.validate_on_submit():
            newanswer = GrantAnswer(
                user = current_user,
                answer = grantanswerform.answer.data,
                grant_question_id=grant_question_id,
                application_id = grant_application_id
                )
            print(f'newanswer is {newanswer.user}')
            print(f'newanswer is {newanswer.answer}')
            print(f'newanswer is {newanswer.grant_question_id}')
            grantanswerform.answer.data = ''
            db.session.add(newanswer)
            db.session.commit()
            flash('Answer has been added', 'success')
            return redirect(url_for('apply_to_grant', grant_id=grant_id, grant_application_id=grant_application_id))
        else:
            print("the form is not valid")

    #logic to enable "submit" button
    submit_button = False
    #counts number of questions to answer
    application_question_total_count = len(grant_questions)
    print(f"application_question_total_count: {application_question_total_count}")
    #counts number of questions answered
    application_answer_total_count = len(answers)
    print(f"application_answer_total_count: {application_answer_total_count}")
    #compare both counts
    if application_answer_total_count == application_question_total_count:
        submit_button = True
    
    #if count is lower : submit button disabled
    elif application_answer_total_count < application_question_total_count:
        pass
    #if count is equal : submit button is enabled
    else:
        print("Something is wrong with count")

    return render_template('grantee/apply-to-grant.html', 
        grant_id=grant_id,
        grant=grant,
        grant_questions=grant_questions,
        grantanswerform=grantanswerform,
        answers=answers,
        answers_from_user_id=answers_from_user_id,
        editanswerform =editanswerform,
        grant_application_id=grant_application_id,
        submit_button=submit_button,
        grant_application=grant_application )

#edit grant answer
@app.route("/edit-grant-answer/<int:grant_id>/<int:grantanswer_id>", methods=['GET', 'POST'])
@login_required
def edit_grant_answer(grant_id, grantanswer_id):
    answer_to_edit = GrantAnswer.query.get_or_404(grantanswer_id)
    application_id = answer_to_edit.application_id

    editanswerform = AnswerGrantQuestionForm(obj=answer_to_edit)
    grantanswerform = AnswerGrantQuestionForm()
    if request.method == 'POST':
        if editanswerform.validate_on_submit():
            editanswerform.populate_obj(answer_to_edit)
            editanswerform.answer.data = ''
            db.session.add(answer_to_edit) 
            db.session.commit()
            flash('Answer has been edited', 'success')
            return redirect(url_for('apply_to_grant', grant_id=grant_id, grant_application_id=application_id))
        else:
            print("the form is not valid")

    return render_template('grantee/apply-to-grant.html', 
        editanswerform=editanswerform,
        grantanswerform=grantanswerform
        )


#delete grant answer
@app.route("/delete-grant-answer/<int:grant_id>/<int:grantanswer_id>",methods=['POST'])
@login_required
def delete_grant_answer(grant_id, grantanswer_id):
    grantanswer = GrantAnswer.query.get_or_404(grantanswer_id)
    grant_application_id = request.form.get('delete_answer_grant_application_id')
    db.session.delete(grantanswer)
    db.session.commit()
    flash('Answer deleted')
    return redirect(url_for(
        'apply_to_grant', 
        grant_id=grant_id,
        grant_application_id=grant_application_id))

#interface to manage grants allocated to user account
@app.route("/manage-grants")
@login_required
def manage_grant():
    return render_template('grantee/manage-grants.html')

#interface to edit or delete to user account
@app.route("/account")
@login_required
def account():
    user = User.query.filter_by(id=current_user.id).first()
    print(f'user = {user.username}')
    return render_template('account.html', user=user)


#delete user account
@app.route("/delete_account")
@login_required
def delete_user_account():
    user = User.query.get_or_404(current_user.id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

#Allows user to contact granter for any question
#PROBLEM : `'MessagingForm' object has no attribute 'validate_on_submit'` this is because I imported the wrong form. 
#Official documentation created this error
#SOlution credits: https://stackoverflow.com/questions/22873794/attributeerror-editform-object-has-no-attribute-validate-on-submit
@app.route('/contact_us', methods=['GET', 'POST'])
@login_required
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
#dashboard
@app.route("/granter-dashboard")
@login_required
def granter_dashboard():
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))

    grants = Grant.query.order_by(Grant.id).all()
    return render_template('granter/granter-dashboard.html',
    grants=grants)

#Create a new grant
@app.route("/create-new-grant", methods=["GET","POST"])
@login_required
def create_new_grant():
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
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
        return redirect(url_for('show_grant', grant_id=newgrant.id))
    else:
        print("the form is not valid")
    return render_template('granter/create-new-grant.html', grantform=grantform)

#Show grant_id content
@app.route('/show-grant/<int:grant_id>', methods=['GET', 'POST'])
@login_required
def show_grant(grant_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
    grant = Grant.query.get_or_404(grant_id)
    list_question = GrantQuestion.query.filter_by(grant_id=grant.id).order_by(GrantQuestion.id).all()
       
    #add grant question
    addquestionform = AddGrantQuestionForm()
    if addquestionform.validate_on_submit():
        print("the form works")
        newquestion = GrantQuestion(
            question = addquestionform.question.data,
            grant_id = grant.id,
           )
        db.session.add(newquestion)
        db.session.commit()
        flash('Question has been added', 'success')
        return redirect(url_for('show_grant', grant_id=grant_id))

    #answer grant question
    answerquestionform = AnswerGrantQuestionForm()
    if answerquestionform.validate_on_submit():
        
        print(f'question_id = {question_id}')
        print("answerquestionform works")
        if question_id:
            newanswer = GrantAnswer(
                answer = answerquestionform.answer.data,
                grant_question_id = question.id
            )
            db.session.add(newanswer)
            db.session.commit()
            flash('Answer has been added', 'success')
            return redirect(url_for('show_grant', grant_id=grant_id))
        
    return render_template('granter/show-grant.html', 
        grant=grant,
        addquestionform= addquestionform,
        list_question=list_question,
        answerquestionform=answerquestionform,
       
        )

@app.route("/activate-grant/<int:grant_id>", methods=['GET', 'POST'])
@login_required
def activate_grant(grant_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))

    grant = Grant.query.get_or_404(grant_id)
    grant.is_active = True
    db.session.commit()
    return redirect(url_for('show_grant', grant_id=grant_id))
    

@app.route("/deactivate-grant/<int:grant_id>", methods=['GET', 'POST'])
@login_required
def deactivate_grant(grant_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))

    grant = Grant.query.get_or_404(grant_id)
    grant.is_active = False
    db.session.commit()
    return redirect(url_for('show_grant', grant_id=grant_id))
    

@app.route("/close-grant/<int:grant_id>", methods=['GET', 'POST'])
@login_required
def close_grant(grant_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
    grant = Grant.query.get_or_404(grant_id)
    grant.is_active = False
    grant.is_closed = True
    db.session.commit()
    return redirect(url_for('show_grant', grant_id=grant_id))
    
@app.route("/create-new-grant/", methods=["GET","POST"])
@login_required
def create_new_grant_question():
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
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
        return redirect(url_for('show_grant', grant_id=newgrant.id))
    else:
        print("the form is not valid")
    return render_template('granter/create-new-grant.html', grantform=grantform)



@app.route('/show_grant/<int:grant_id>/questions/<int:grantquestion_id>/edit',methods=['GET', 'POST'])
@login_required
def edit_show_grant_question(grant_id, grantquestion_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
    question = GrantQuestion.query.get_or_404(grantquestion_id)
    editquestionform = EditGrantQuestionForm(obj=question)
    if editquestionform.validate_on_submit():
        question.question = editquestionform.question.data
        db.session.commit()
        flash('Question updated successfully!', 'success')
        return redirect(url_for('show_grant', grant_id=grant_id))
    
    
    return render_template('granter/edit_question.html', 
        question=question,
        editquestionform=editquestionform,
            )

@app.route('/show_grant/<int:grant_id>/questions/<int:grantquestion_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_show_grant_question(grant_id, grantquestion_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
    question = GrantQuestion.query.get_or_404(grantquestion_id)
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted', 'success')
    return redirect(url_for('show_grant', grant_id=grant_id))

#allows granter to see all applictaions against grant id
@app.route("/show-all-grant-application/<int:grant_id>")
@login_required
def show_all_grant_application(grant_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
    applications = (GrantApplication.query.filter_by(grant_id=grant_id, is_submitted = True)).filter(GrantApplication.user_id.isnot(None)).all()
    grant = Grant.query.filter_by(id=grant_id).first()
    for grantapplication in applications:
        print(f"grant id  = {grantapplication.grant_id} +applications = {grantapplication.id} + user_id = {grantapplication.user_id} ")

    return render_template('granter/show-all-grant-application.html',
    grant=grant,
    grant_id=grant_id,
    applications=applications)

@app.route("/show-user-grant-application/<int:grant_id>/<int:grant_application_id>",methods=['GET', 'POST'])
@login_required
def show_user_grant_application_id(grant_id, grant_application_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
    
    #logic to retrieve user ID of grant application
    grant_application = GrantApplication.query.filter_by(id=grant_application_id).first()
    user_id = grant_application.user_id

    #logic to list all questions and related answers
    grant_question = GrantQuestion.query.filter(GrantQuestion.grant_id == grant_id).order_by(GrantQuestion.id).all()
    grant_question_user_answer = []
    for grantquestion in grant_question:
        user_answers = GrantAnswer.query.filter_by(grant_question_id=grantquestion.id, user_id=user_id).all()
        grant_question_user_answer.append({
            'question':grantquestion.question,
            'answer':[answer.answer for answer in user_answers]
        })


    return render_template('granter/show-user-grant-application.html',
    grant_question_user_answer=grant_question_user_answer,
    grant_question=grant_question,
    grant_id=grant_id,
    grant_application_id=grant_application_id,
    user_id=user_id)

@app.route("/reject-user-grant-application/<int:grant_id>/<int:grant_application_id>",methods=['GET', 'POST'])
@login_required
def reject_user_grant_application_id(grant_id, grant_application_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))

    application = GrantApplication.query.get_or_404(grant_application_id)
    application.is_rejected = True
    db.session.commit()
    return redirect(url_for('show_all_grant_application',
    grant_id=grant_id,
    grant_application_id=grant_application_id))

@app.route("/approve-user-grant-application/<int:grant_id>/<int:grant_application_id>",methods=['GET', 'POST'])
@login_required
def approve_user_grant_application_id(grant_id, grant_application_id):
    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))
    #TO DO: ADD CHECK TO MAKE SURE ONLY 
    #THE GRANTER CAN PERFORM THIS ACTION AS CURRENT USER
    application = GrantApplication.query.get_or_404(grant_application_id)
    application.is_approved = True
    db.session.commit()
    return redirect(url_for('show_all_grant_application',
    grant_id=grant_id,
    grant_application_id=grant_application_id))

#Add logic to set GrantApplication as Submitted by user when
#all question have been answered
#count all questions within Application ID
#If all questions are answered then show "Submitted button"
#if user clicks submits button, application ID moves from Pending to Submitted

#Add logic to set GrantApplication as approved or rejected by Granter

# Set FLASK_ENV as production or dev. environement
if os.environ.get('FLASK_ENV') == 'development':
    app.config['DEBUG'] = True
    print("Running in development mode")
else:
    app.config['DEBUG'] = False
    print("Running in production mode")

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])
