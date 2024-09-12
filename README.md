# M3Project

TODO:

IN Login form CSRF token message in browser console : ask Gareth.
remove uncommented stuff (grants-available)
Say that in addgrant and other models where therei s interger, the value is capped to -2,147,483,648 to 2,147,483,647. Adding superior numbers would cause a `400` error. To avoid getting the error, I added some javascript at the bottom of the page that checks and disbale submit button if the value is higher than it should.
add design for back button
Explain why grants cant be deleted
Explain that it would make sense the granter cannot deactivate a grant after activating it.
if time (or explain in readme): correct repetition in css for `status-colour-...`
Missing : retrieve password system
add email system when application is rejected or approved or submitted
add grantis closed to close applications when needed.
Add search function + pagination for grants
remove grant-management references if not used before submission
Add check to make sure user wants to delete something before pressing button
Add Django style admin panel
Prevent user from deleting application once approved but rather create another status as "withdrawn"
Talk about contact us feature

TO DO:
Make single column container two columns instead from 992px
IN dhasboard change grants available rows width and contrsain it to body
Add footer
Add ERD
Add delete appluctaion for granter if application not active
removae manage grants from navbar
fix collapse menu in navbar so its not transparent
Remove contact us from navbar
Add search function to dashbaords + grants available

Title - Grant Management

View the live site: https://grant-management-mp3-709b64ecedb2.herokuapp.com/

COLOUR PALETTE
#264653
#2A9D8F
#E9C46A
#F4A261


# Table of Contents

1. [User Experience](#ux)
   - [Project Goals](#project-goals)
     * [User Goals](#user-goals)
     * [Site Owner Goals](#site-owner-goals)
   - [User Stories](#ux-subsection)
     * [Local Business](#local-business)
     * [Public Sector](#public-sector)
     * [Users](#user)

2. [Design](#design)
   - [Colours](#colours)
   - [Typography](#typography)
   - [Icons & Images](#icons-images)
   - [Wireframes](#wireframes)
   - [Databases](#databases)

3. [Features](#features)
   - [Authentication](#auth)
   - [Admin Panel](#admin-panel)
   - [Create Grant](#create-grant)
   - [Create Grant Questions](#create-grant-questions)
   - [Read, Edit & Delete Grant Questions](#read-edit-delete-grant-questions)
   - [Create Grant Application](#create-application)
   - [Read, Edit & Delete Application](#read-edit-delete-application)
   - [Submit Application](#submit-application)
   - [Approve & Reject Application](#approve-reject-application)
   - [CSRF Token](#csrf-token)
   - [Context Processor](#context-processor)
   - [Currency Display](#currency-display)
   - [Decorators](#decorators)
   - [WTForms](#wtf)
   - [Customer Error Pages](#error-pages)
   - [Navbar](#navbar)
   

 
4. [Technologies](#tech)

5. [Testing](#testing)
   - [Validator Testing](#val-testing)
     * [HTML](#html)
     * [CSS](#css)
     * [Javascript](#js)
   - [Lighthouse Testing](#lighthouse-testing)
   - [User Testing](#user-testing)

6. [Bugs](#bugs)
   - [Current bugs](#current-bugs)
   - [Design & User Experience improvements](#design-improvements)
   - [Logic improvements](#logic-improvements)
     
7. [Deployment](#deployment)

8. [Credits](#credits)






## 1. User Experience <a name="ux"></a>

There are three types of users for this product. The actual user applying looking to apply for a grant (the "Grantee"), the user issuing and validating granter applications (the "Granter") and the administrator.

### 1.1 Project Goals <a name="project-goals"></a>


#### 1.1.1 User Goals & Expectations <a name="user-goals"></a>

The goal of this product is to offer a platform to people to apply for grant with local authorities. 

With the exception of large granting bodies, grants are still applied to by email. 

This makes it hard for grantees to know what is available, and also harder for granters who still need to look into their emails to find applications: this causes a second problem around document control.

The whole grant validation and management process is a very long process, which could be split into 2 mains phases:
* Phase 1 - Grant creation and grant application. This phase includes the creation and the publication of the grant, by the Granter, and the application phase by the Grantee all the way to grant validation or rejection by the Granter.
* Phase 2 - Grant Management. This phase includes the management of reporting documentation from both parties together with communication.

Note: Although it was my intention to cover both phases in this project, I have come to realise, Phase 1 was already a longer piece than anticipated. As a result, this product will address Phase 1 only.

### 1.2 User Stories <a name="user-goals"></a>

* As the administrator I want to assign a Granter role to accounts registered as Grantee as default.

* As a granter, I want all people accessing my grants to be logged in, for analytics purposes. 

* As a granter, I want to create a grant and attach any number of questions to it. 
* As the administrator I want to be able to link questions to grants and their issuing granter.

* As a granter, I want to be able to edit or delete questions.

* As a granter, I want to decide the grant status: whether it is innactive (not ready to be published), active (published) and close whenever my fund has run out (closed). 

* As a grantee, I want to be able to create an account and apply to any available grant.

* As a grantee, I want to be able to answer grant questions, edit or delete them

* As a grantee, before or after submitting my application I want to be able to review my application.

* As a granter, I do not want submitted application to be editable.

* As a granter, I do not want application to be submitted against grants with a status of "closed".

* As a granter, I want to be able to review application and either approve or reject the appplication.

* As a grantee, I want to be kept up to date of my application whether the application is still pending, approved or rejected. 



## 2. Design <a name="ui"></a>

The design is simple and avoids using images.

### 2.1 Colours <a name="colours"></a>
As this is a coprorate product, colours used are simple, but also add some sense excitment through bright yellow and orange.

![Colour Palette](documentation/colour-palette/colour-palette.png)

### 2.2 Typography <a name="typography"></a>
Typography follows the same principle as the colours with the use of Poppins and Nerko One.

We have selected Google Fonts, instead of custom fonts, to benefit from better support.

This font can be found on: https://fonts.google.com/

### 2.3 Icons & Images <a name="icons-images"></a>

No static images were used for this project.

Credits need to however be given to Fontawesome for their icons: https://fontawesome.com/

### 2.4 Wireframes <a name="wireframes"></a>

**Sign Up**

**Register**

**Grantee Dashboard**

<img src="" alt="" width="320px">

**Grants Available**

<img src="" alt="" width="320px">

**Apply to Grante**

<img src="" alt="" width="320px">

**Granter Dashboard**

<img src="" alt="" width="320px">

**Create Grant Dashboard**

<img src="" alt="" width="320px">

**See Grant Applications**

<img src="" alt="" width="320px">

**Read Specific Applications**

<img src="" alt="" width="320px">

### 2.5 Databases <a name="databases"></a>

The models define the structure and relationships of entities in the application. 

These entities include users, grants, grant applications, questions related to grants, and answers to those questions. 

Each model corresponds to a table in a PostgreSQL database.

**ER Diagram**

<img src="documentation/erd/flask - ERD.png" alt="" width="320px">

**1. UserType Enum**

UserType is an enumeration used to distinguish between the two user types: "Grantee" and "Granter".

This enum is associated with the user_type field in the User model to indicate the type of user, leading to specific permissions in the business logic.

**2. User Model**

Represents the users of the system: Grantees and Granters.

Fields:
id: Primary key, unique identifier for each user.
username: Unique username of the user.
password: User's password (likely stored hashed).
email: Unique email of the user.
company_name: Company name (optional).
user_type: Either "Grantee" or "Granter" as per the UserType enum.
created_on: Timestamp of when the user was created.
Relationships:
Grants: A User (acting as a granter) can have many grants associated with them (usergrants).
GrantApplications: A User (acting as a grantee) can submit multiple grant applications (usergrantapplications).
GrantAnswers: A User can submit multiple answers to grant questions (usergrantanswers).

**3. Grant Model**

Represents a grant that is available for applicants to apply for.

Fields:
id: Primary key, unique identifier for each grant.
user_id: Foreign key linking to the User (granter) who created the grant.
grant_title: Title of the grant.
grant_description: Description of the grant.
grant_fund: Amount of funds available for the grant.
created_on: Timestamp of when the grant was created.
is_active: Indicates if the grant is currently active.
is_closed: Indicates if the grant is closed for applications.

Relationships:
User: The Grant model has a foreign key relationship with User (granter).
GrantQuestions: A grant can have multiple questions (questions) linked to it.
GrantApplications: A grant can have multiple applications (applications) linked to it.

**4. GrantQuestion Model**

Represents a question associated with a grant that applicants need to answer.

Fields:
id: Primary key, unique identifier for each question.
user_id: Foreign key linking to the User who created the question (granter).
grant_id: Foreign key linking to the Grant the question is associated with.
question: The actual question text.
created_on: Timestamp of when the question was created.

Relationships:
Grant: A question belongs to a specific grant (grant).
GrantAnswers: A question can have multiple answers (answers) submitted by applicants.

**5. GrantApplication Model**

Represents an application that a user (grantee) submits for a grant.

Fields:
id: Primary key, unique identifier for each application.
user_id: Foreign key linking to the User who submitted the application (grantee).
grant_id: Foreign key linking to the Grant the application is for.
is_submitted: Boolean indicating if the application has been submitted.
is_approved: Boolean indicating if the application has been approved.
is_rejected: Boolean indicating if the application has been rejected.

Relationships:
Grant: The application is linked to a specific grant id.
User: The application is submitted by a specific user id.
GrantAnswers: An application can have multiple answers submitted by a User.

**6. GrantAnswer Model**

Represents an answer to a question in a grant application.

Fields:
id: Primary key, unique identifier for each answer.
user_id: Foreign key linking to the User who submitted the answer.
application_id: Foreign key linking to the GrantApplication the answer is attached to.
grant_question_id: Foreign key linking to the GrantQuestion being answered.
answer: The actual answer text.
created_on: Timestamp of when the answer was created.

Relationships:
User: The answer is submitted by a specific user.
GrantApplication: The answer belongs to a specific application.
GrantQuestion: The answer is associated with a specific question.

**Interactions Between Models**

User can CRUD(Create,Read,Update,Delete) grants, questions, applications and answers.

A grant can have multiple associated questions for applicants to answer.

Each grant can also have multiple applications.


## 3. Features <a name="features"></a>

### 3.1 Authentication <a name="auth"></a>

**is_authenticated**: Both login and register functions redirect the user to their respective dashboard, should they happen to reach the login or register page whilste authenticated:

    if current_user.is_authenticated:      
            if current_user.user_type == UserType.GRANTER:
                return redirect(url_for('granter_dashboard'))
            elif current_user.user_type == UserType.GRANTEE:
                return redirect(url_for('dashboard'))

**Login**: The login function can be found in `def index()`

It is linked to the User Model, through `UserLoginForm()`.

Documentation and sources used can be found below.

The following command will need to be run:
    `pip install Flask-Login` (https://pypi.org/project/Flask-Login/)
    `pip install bcrypt` - used to hash passwords (https://pypi.org/project/bcrypt/)

**Register**: The registration process is delivered by `def register()` and leverages the use of `UserRegisterForm`.

In order to improve the user experience, a few validators were implemented through the flask form. In addition, some javascript was also implemented at the bottom of `register.html` to render the form requirements into actions to the end user.

Note of errors encountered: Some special characters were not included at the first iteration of validators. Making any password like `mypassword!1` invalide.

The below code was inspired from answer to this github post (credits : https://gist.github.com/frizbee/5318c77d2084fa75cd00ea131399581a)

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


To avoid the 500 error, checks were added to function if username or email address is already used:

    if existing_user:
            flash('Username already exists.', 'danger')
            return render_template('register.html', form=form)

### 3.2 Admin Panel <a name="admin-panel"></a>

For the purpose of this project a basic admin panel with limited action was created and can be found in `admin()`.

The pannel allows for user to change their status from grantee to granter, and granter to grantee.

This panel was solely built for the purpose of the examination of the project to give examinator easy access to both user type.

As the project will be accessible on github, the admin panel does not allow for user account deletion, to avoid outside user deleting all users from the admin panel.

To delete a user account, one need to log-in with the user credentials and find the "delete" option in Account Details section in Navbar.

As part future development, it would make sense to build a superuser function and have a django style admin panel.

To access admin panel simply follow these steps:
* Register an account
* To the root url add `admin`. (for example: http://127.0.0.1:5500/admin)

You will be prompted to the following page, where with, for each user, their current user type in the middle column and the possibility to switch to another user type in the right column.

By clicking on the other user type in the right column, the related user account will change from one type to the other.

<img src="documentation/screen-shots/admin-panel.png" alt="change user type in admin panel" width="320px">


### 3.3 Create Grant <a name="create-grant"></a>
This functionnality is only available to Granter and is triggered `create_new_grant().

The function starts by checking user type. If the user type is not Granter, it will redirect the user to the Grantee dashboard:

    if current_user.user_type != UserType.GRANTER:
        return redirect(url_for('dashboard'))

Note: this logic is repeated for every granter related function. As part of future development, it would be interesting to look at a way to create a `@granter_only` decorator, or maybe simply creating a second app for Granters with a specific dashboard through an API.

The rest of the function leverages `AddGrantForm()` to create Grant model objects and populate each field.

Upon successful creation of the grant, Granter is redirected to `show_grant()` to create related questions.

### 3.4 Create Grant Questions <a name="create-grant-questions"></a>

This functionnality is only available to Granter and is triggered `show_grant()`. The function take the newly created `grant_id` as a parameter.

    def show_grant(grant_id):

It allows granter to see the granter they have created and any number of questions to it, using `AddGrantQuestionForm`.

Questions are then listed on the template through `list_question` variable, which returns all GrantQuestion in the database that match the filter of `grant_id` parameter.

    list_question = GrantQuestion.query.filter_by(grant_id=grant.id).order_by(GrantQuestion.id).all()

This page also allows the granter to manage the grant itself.

From this page, it can see the current status of the grant (inactive, active or closed), and change this status to the next one.

Note: Once a grant is moved from inactive to active, the granter cannot de-activate it and can only close it.

Once closed, the grant can only be re-activated.

<img src="documentation/screen-shots/show-grant.png" alt="display specific grant management page to granter" width="320px">

### 3.5 Read, Edit & Delete Grant Questions <a name="read-edit-delete-grant-questions"></a>


### 3.6 Create Grant Application <a name="create-application"></a>
### 3.7 Read, Edit & Delete Application <a name="read-edit-delete-application"></a>
### 3.8 Submit Application <a name="submit-application"></a>
### 3.9 Approve & Reject Application <a name="approve-reject-application"></a>
### 3.10 Approve & Reject Application <a name="approve-reject-application"></a>
### 3.11 CSRF Token <a name="csrf-token"></a>
### 3.12 Context Processor <a name="context-processor"></a>
### 3.13 Currency Display <a name="currency-display"></a>
### 3.14 Decorators <a name="decorators"></a>
### 3.15 WTForms <a name="wtf"></a>
### 3.16 Customer Error Pages <a name="error-pages"></a>
### 3.17 Navbar <a name="navbar"></a>






////

**Navbar**
The Navbar displays 2 different version based on the UserType.

Passing a logic like `  {% if current_user.user_type == UserType.GRANTEE %}` wasnt sufficent to make `UserType` available in if statements.

In order to make UserType available, a `context processor` had to be injected.

Documentation: https://flask.palletsprojects.com/en/2.3.x/templating/

    @app.context_processor
    def inject_user_type():
        return dict(UserType=UserType)

**Currency Display**
Doucmentation: https://flask.palletsprojects.com/en/1.1.x/templating/

Additional help: https://stackoverflow.com/questions/12078571/jinja-templates-format-a-float-as-comma-separated-currency

App.py:
    @app.template_filter('currency')
    def currency_filter(value):
        try:
            return f"£ {value:,.2f}"
        except (ValueError, TypeError):
            return value

Add filter in template: `| currency`

    {{ grantapplication.grant.grant_fund | currency }}


**@login_required decorator**

**Extends template**
Documentation : https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/

**Navbar**
Documentation
https://getbootstrap.com/docs/4.0/components/navbar/

**Error page handling**
For errors: 404 and 500 only

Templates for error 404 can be found on this path: `M3Project\templates\error-handling\404.html`

Templates for error 505 can be found on this path: `M3Project\templates\error-handling\500.html`

Redirection:
As there are two dashboards depending on the user identity, the `home` button returns the user to the original login page.

To achieve this, the code retruns the user to `index()`, which filters whether the user is authenticated or not. If it is, a redirection is made to either `dashboard()` or `granter_dashboard()`.

**WTF Forms**
    https://wtforms.readthedocs.io/en/3.1.x/
    https://flask.palletsprojects.com/en/3.0.x/patterns/wtforms/

    Mention use of validators to display messages when form is not compeleted

    Use of CSRF Token
    from flask_wtf.csrf import CSRFProtect
    import os
    from flask import flash (to display toast like messages)

    Encountered problem: In production, the self generated token does not work (`app.config['SECRET_KEY'] = os.urandom(24).hex()`).

    I had to generate a unique token and add it to Heroku's envorionment variables.

    To generate this unique token I used the following link: https://djecrety.ir/

    Other problem: `[DOM] Found 2 elements with non-unique id #csrf_token`

    instead of `{{ form.csrf_token }}`, I had to update from documentation to :`form.csrf_token()`.



    Credits: 
    #WTF Documentation to set up CSRF Token : https://flask-wtf.readthedocs.io/en/0.15.x/csrf/
    #Additional Credits to set up CSRF Token : https://stackoverflow.com/questions/34902378/where-do-i-get-secret-key-for-flask
    #Found 2 elements with non-unique id #csrf_token: https://www.reddit.com/r/flask/comments/gtjwbt/two_forms_csrf_token_nonunique_id_chrome_warning/

**Data base**
`pip install flask-sqlalchemy`
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

Being used to django, Flask-Migrate seem to offer the same functionality of writting up migration
`pip install Flask-Migrate`
https://flask-migrate.readthedocs.io/en/latest/

Initial command : `$ flask db init`
Following command: `$ flask db migrate -m "Initial migration."`
To apply migrations: `$ flask db upgrade`

Problem encountered: 
In `app.config['SQLALCHEMY_DATABASE_URI'] =`, I had to specify the full path as the project is hosted on OneDrive which causes problems. If the project was hosted directly on local machine, I should be able to have the relative path.

Set up of PostGres on Local
`pip install psycopg2`
https://medium.com/@shahrukhshl0/building-a-flask-crud-application-with-psycopg2-58de201e3c14

**Create environement variables & Setup PostGres on local**
To avoid password being leaked on github when the code is pushed, we use variables which are stored in files that are not pushed to git hub.

documentation: https://pypi.org/project/python-dotenv/

To do this: 
`pip install python-dotenv`

Add:
`...
from dotenv import load_dotenv
...
load_dotenv()
...
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url

Create `.env` file in root directory and the following line:
`DATABASE_URL=postgresql://[username]:[postgres-password]@localhost/[databasename]`

Note the change for `database_url`. This is due to a problem faced during the deployment on Heroku returning the following message:
`sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres`

This error is due to a change in Sqlalchemy library which has not been reflected with Heroku. The library now requires a reference to `postgresql` which Heroku still refers as `postgres`.

As a result, in order for the library to work on heroku an if statement has been added to the code, which handles this situation.

Another solution could have been to roll the library back to a version prior to <1.4.0 (1.3.23 is the last 1.3.x release).

Credit for solution: https://stackoverflow.com/questions/66690321/flask-and-heroku-sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy


**Heroku Setup**
INstall heorku commandline (CLI): https://devcenter.heroku.com/articles/heroku-cli
Run `pip install gunicorn` on terminal
INstall PostGres: `pip install psycopg2`
Set up requirements.txt file: `pip freeze > requirements.txt`
Create Procfile: `echo web: gunicorn app:app > Procfile`
Login into Heroku: `heroku login`
Create projet on heroku: `heroku create grant-management-mp3`

Problem encountered: the Procfile generated with command line from documentation ``echo web: gunicorn app:app > Procfile` created an issue, which seems to be relating to encoding: which defaulted to UTF-16 instead of UTF-8.

To solve my problem, I created a new Procfile through a Notepad, selected encoding UTF-8 and called it `Procfile.txt` in the same location as the actual Procfile. I then deleted the previous Procfile and renamed `Procfile.txt` to `Procfile`.

Credits: https://stackoverflow.com/questions/19846342/unable-to-parse-procfile

**Heroku Migration**
A migration will need to be made to heroku from your local repository: ` heroku run flask db upgrade`

**Developement & Production Environements**
Documentation: https://flask.palletsprojects.com/en/1.1.x/config/
Step up
To set up the app as development of production, the following code is implemented:
app.py:
    import os
    if os.environ.get('FLASK_ENV') == 'development':
        app.config['DEBUG'] = True
        print("Running in development mode")
    else:
        app.config['DEBUG'] = False
        print("Running in production mode")

    if __name__ == "__main__":
        app.run(debug=app.config['DEBUG'])

In the same `.env` file created in the previous section (**Create environement variables & Setup PostGres on local**) add the following variables:
    FLASK_ENV=development
    FLASK_DEBUG=1

These variables are for development only.

To set up production on heroku, the following variables need to be added to Heroku variables.

These variables can be defined in settings in the heroku dashboard. (Look for `Config Vars` section) then add the following:
FLASK_ENV = production
FLASK_DEBUG = 0

To check if it works, when running the project on local (or development) the following messages will print on the console:
    Running in development mode
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    Running in development mode
    * Debugger is active!

In heroku the following line will be printed in the logs:
`Running in production mode`


**User types**
`from enum import Enum`
https://docs.python.org/3/library/enum.html

**Foreign Keys**
FK problem
Note: in `class GrantAnswer(db.Model)` the foreign key applied to field `grant_question_id` is `grant_question.id`. It seems running `flask db migrate` autorenamed the table generated by `class GrantQuestion(db.Model)` to `grant_question. This was found out by checking migration file: #bdd8261021d8.

**Grantee Interface**
Only accesses grants that are "active". This is achieve in `grant_available()`:
    grants = Grant.query.filter_by(is_active=True)

**Granter Interfance**

**Display of application**
Because I didnt want the applications to be destroyed when a user deletes their account, it creates some display challenges.

On some occasion, I had to add an additional filter to remove all application where user_id is not `none`.

Example:

    #allows granter to see all applictaions against grant id
    @app.route("/show-all-grant-application/<int:grant_id>")
    @login_required
    def show_all_grant_application(grant_id):
        if current_user.user_type != UserType.GRANTER:
            return redirect(url_for('dashboard'))
        applications = (GrantApplication.query.filter_by(grant_id=grant_id, is_submitted = True)).filter(GrantApplication.user_id.isnot(None)).all()

Credit for user of .filter() : https://stackoverflow.com/questions/32071527/elegant-way-to-filter-by-none-or-not-none

**CRUD**
CRUD is present in a few pages. The below details the CRUD functionality applied to apply_to_grant(), as this was the most complex part of the project.

**Create**
To answer a specific question, the user populates a form.

The form is defined as a FlaskForm

    class AnswerGrantQuestionForm(FlaskForm):
        answer = StringField("Enter Answer", validators=[DataRequired(),])
        submit = SubmitField('Submit')

In this example, the form is aimed at populating model `GrantAnswer`

This model works in conjunction with 3 others models

    class User(db.Model,UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        ...

    class Grant(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        ...

    class GrantQuestion(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        user = db.relationship('User', backref='usergrantquestions')
        grant_id = db.Column(db.Integer, db.ForeignKey('grant.id'))
        grant = db.relationship('Grant', backref='questions')
        question = db.Column(db.String(200), nullable=False)
        created_on = db.Column(db.DateTime, default=datetime.utcnow)
        answers = relationship('GrantAnswer', backref='question', lazy=True)

    class GrantAnswer(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        user = db.relationship('User', backref='usergrantanswers')
        grant_question_id = db.Column(db.Integer, db.ForeignKey('grant_question.id'))#the FK was automatically named `grant_question` in the migration.
        grant_question = relationship('GrantQuestion', back_populates='answers')
        answer = db.Column(db.String(300), nullable=False)
        ..

Logic
When populationg this form, it is important to keep in mind ForeignKey with `GrantQuestion` and `User`.

As a result, some additional logic needs to take place in both the apply_to_grant() and its template.

In the function, we need to capture:
`gantquestion.id`, which can be obtained through the loop
`answer`, which is captured through the form field
`user`, which is captured through `current_user`

    grantanswerform = AnswerGrantQuestionForm()
    if request.method == 'POST':
        grant_question_id = request.form.get('grant_question_id')
        #answer_form = None
        if grantanswerform.validate_on_submit():
            newanswer = GrantAnswer(
                user = current_user,
                answer = grantanswerform.answer.data,
                grant_question_id=grant_question_id,
                )
            print(f'newanswer is {newanswer.user}')
            print(f'newanswer is {newanswer.answer}')
            print(f'newanswer is {newanswer.grant_question_id}')
            grantanswerform.answer.data = ''
            db.session.add(newanswer)
            db.session.commit()
            flash('Answer has been added', 'success')
            return redirect(url_for('apply_to_grant', grant_id=grant_id))
        else:
            print("the form is not valid")

Template logic
The template of the form adds the following elements:
`csrf_token`, adding extra protection, this field is invisibile to the user
a hidden input field, which passes the `grantquestion.id` as a value. This value is then captured in the form logic.
the user answer with `answer`

    <form method="POST" action="">
    <input type="hidden" name="grant_question_id" value="{{ grantquestion.id }}">
        {{ grantanswerform.csrf_token }}
        {{grantanswerform.hidden_tag()}}
        {{grantanswerform.answer}}
    
        {{grantanswerform.submit}}
    
    </form>



**Read**
I wanted to avoid restricting the number of question to a number set in the GrantQuestion model.

I wanted to allow the granter to create as many question as they wanted.

This caused a few problem as I also wanted to set an answer field to each question.

This resulted in having to create 2 models : GrantQuestion (with a FK to Grant ID) and AnswerQuestion.

    class Grant(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        ...

    class GrantQuestion(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        user = db.relationship('User', backref='usergrantquestions')
        grant_id = db.Column(db.Integer, db.ForeignKey('grant.id'))
        grant = db.relationship('Grant', backref='questions')
        question = db.Column(db.String(200), nullable=False)
        created_on = db.Column(db.DateTime, default=datetime.utcnow)
        answers = relationship('GrantAnswer', backref='question', lazy=True)

    class GrantAnswer(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        user = db.relationship('User', backref='usergrantanswers')
        grant_question_id = db.Column(db.Integer, db.ForeignKey('grant_question.id'))#the FK was automatically named `grant_question` in the migration.
        grant_question = relationship('GrantQuestion', back_populates='answers')
        answer = db.Column(db.String(300), nullable=False)
        ..

The questions are displayed based on the Grant_id of the URL. Based on this grant id, I run an intial loop through GrantQuestion, which returns all questions attached to a specific grant iD.

NExt steps proved to be trickier. I wanted to display either the user's answer to the specific grant, if they had answered already, or display a answer field.

To do this, I needed to create a nested loop, which would loop through all the answers with a common GrantQuestion_id and filter the `current_user` answers and return them.

To achieve this, I created a first variable `answers` which would return all answers against `current_user` and `GrantQuestion.id`

answers = GrantAnswer.query.join(GrantQuestion).filter(
        GrantQuestion.grant_id == grant_id,
        GrantAnswer.user_id == current_user.id
    ).all()

I was suggested to look at `Dictionary Comprehension` to solve my problem.

The clearest definition I found is the following (form:https://www.datacamp.com/tutorial/python-dictionary-comprehension ):"Dictionary comprehension is a method for transforming one dictionary into another dictionary. During this transformation, items within the original dictionary can be conditionally included in the new dictionary, and each item can be transformed as needed."

`dict_variable = {key:value for (key,value) in dictonary.items()}`

I therefore created a second variable:
`answers_from_user_id = {answer.grant_question_id: answer for answer in answers}`

`answer` represents each object within `GrantAnswer`
`answer.grant_question_id` returns the ID of each `answer` and is the `key` of the comprehension.
`answer` (first one) represents the value
`answer` (second one) represents the (key,value)
`answers` is the dictionary created through the variable of the same name.


This `` variable allowed me to return the correct result which looks like this in the console:
`print(answers_from_user_id) ={1: <GrantAnswer: <Grant: <Grant 1 Grant1Description 35000> Grant 1 Question 1> Answer 1 to Grant1 Question1>}`

However, in order to apply this to the template additional steps where needed.

An intial forloop over `grantquestion` was created. 

    {%for grantquestion in grant_questions%}
    {%endfor%}

As a second step a condition check is performed, looking for a `grantquestion_id` answered by `current_user` in the newly created dictionary `answers_from_user_id`.

    {%for grantquestion in grant_questions%}
        {% if grantquestion.id in answers_from_user_id %}
        {%endif}
    {%endfor%}

As a final step, to display the answer in a satisfying mannger in the template, I call `{{ answers_from_user_id[grantquestion.id].answer }}`

    {%for grantquestion in grant_questions%}
        {% if grantquestion.id in answers_from_user_id %}
            <p>Your Answer: {{ answers_from_user_id[grantquestion.id].answer }}</p>
        {%endif}
    {%endfor%}


Which returns the `current_user` answer with matching grantquestion.id.

If this answer does not exists, it template returns a form.

**Update**

**Delete**
Deletion of a grant answer is handle in `delete_grant_answer()` which takes the parameters of `grant_id`, `grantanswer_id`.

Considering `grantanswer_id` already has a specific id having `grant_id` in the path is not fully necessary except for ease of access for the `return redirect()`.

`return redirect()` returns the user to the grant_id template the answer was originally deleted from. To achieve this, values of `grant_id` and `grant_application_id` are used. `grant_id` is extracted from the function's parameter, and `grant_application_id` is taken from the the template (`<input type="hidden" name="delete_answer_grant_application_id" value="{{ grant_application_id }}">`) and returned in the function through variable `grant_application_id = request.form.get('delete_answer_grant_application_id')`.


**Note** - For `delete_application()`, I didnt created a form and couldnt call the hidden_tag from WTF forms.

In order to hide the CSRF token, I added it to a hidden input:
`<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">`

I am not sure if this could create security issues. Looking at a few posts on stackover flow, it does not seem to compromise security:
https://stackoverflow.com/questions/68289406/flask-hidden-input-field-with-csrf-token-is-visible-in-elements-pane
https://stackoverflow.com/questions/32620613/if-a-csrf-token-is-placed-inside-a-hidden-input-isnt-it-possible-for-a-malicio


**Note - Cascade**
When deleting the application ID, the answers remained in the database and were rendered in the next application.

In order to remove the answer objects (child) associated with the application object (parent), `cascade` was implemented.

documentation: https://docs.sqlalchemy.org/en/20/orm/cascades.html

In the sample below `cascade='all, delete-orphan'` will delete all child objects associated with parent object.

    class GrantApplication(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        answers = db.relationship('GrantAnswer', backref='grant_application', cascade='all, delete-orphan')


    class GrantAnswer(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        application_id = db.Column(db.Integer, db.ForeignKey('grant_application.id'))
        application = db.relationship('GrantApplication', backref='userapplications')


NOTE: Say I wanted to apply the method to all models, but resulted in a number of errors. Didnt have time to do it. Only this relationship needed `cascade` implemented for the project to work.

**Application Status**
When a user creates an application, the application is given an `ID` and is default value of `False` against `is_submitted field.

    class GrantApplication(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        user = db.relationship('User', backref='usergrantapplications')
        grant_id = db.Column(db.Integer, db.ForeignKey('grant.id'))
        grant = db.relationship('Grant', backref='applications')
        is_submitted = db.Column(db.Boolean, default=False)

This status is updated to `True` when all question listed a the `grant_id` Foreign Key the application is assigned against, which is achieved through `submit_application()`.

In order to avoid a users submitting someone else application by using the path in the URL, the function also checks if `the user_id` registered agianst the `application_id` is `current_user`, before marking an application as submitted.

    if submitted_application_user_id == current_user.id:
            submission = GrantApplication(
            user_id = current_user.id,
            grant_id = grant_id,
            is_submitted = True
        )

Depending on the status of the application, template: `grants-available.html` displays different options.

Once the application has been submitted, the user can either delete or read the application with `read_submitted_application()`

**Credits**
DB Beaver for ERD generator : https://dbeaver.com/docs/dbeaver/ER-Diagrams/

**To improve**
MIgrations : I made a few mistakes with the foreign keys, in particular when trying to establish relationships. I had to delete the migrations and restrat from strach on a few occasions, as I didnt know how to fix my problems from the migration files.