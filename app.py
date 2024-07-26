from flask import Flask, render_template
from wtforms.form import Form
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import os
app = Flask(__name__)
app.run(debug=True)

#Messaging System 
#This is used to create messages between grantee and granter
#WTF Documentation to set up CSRF Token : https://flask-wtf.readthedocs.io/en/0.15.x/csrf/
#Additional Credits to set up CSRF Token : https://stackoverflow.com/questions/34902378/where-do-i-get-secret-key-for-flask
app.config['SECRET_KEY'] = os.urandom(24).hex()
csrf = CSRFProtect(app)


class MessagingForm(FlaskForm):
    #TODO: automatically add username without user input later on
    username = StringField("Provide name", validators=[DataRequired()])
    #TODO: if message is related to specific grant ID, add logic to pass ID field
    message = StringField("Provide message", validators=[DataRequired()])
    submit = SubmitField('Submit')


# Authentication logic
@app.route("/")
def index():
    return render_template('index.html')

# Error Page Handling
@app.errorhandler(404)
def page_not_found_error(e):
    print("page_not_found_error()")
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
    form = MessagingForm()
    
    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ''
    return render_template('grantee/contact-us.html',
        username = username,
        form = form)

# Granter Interface Logic

if __name__ == "__main__":
    app.run(debug=True)
