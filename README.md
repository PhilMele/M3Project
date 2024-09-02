# M3Project

TODO:
Set debug to false when in production
add email system when application is rejected or approved or submitted
add extra panel for granter to see as grantee
add admin section to change user type from grantee to granter


COLOUR PALETTE
#264653
#2A9D8F
#E9C46A
#F4A261
#E76F51

Features
**Navbar**
The Navbar displays 2 different version based on the UserType.

Passing a logic like `  {% if current_user.user_type == UserType.GRANTEE %}` wasnt sufficent to make `UserType` available in if statements.

In order to make UserType available, a `context processor` had to be injected.

Documentation: https://flask.palletsprojects.com/en/2.3.x/templating/

    @app.context_processor
    def inject_user_type():
        return dict(UserType=UserType)

**Login**
`pip install Flask-Login`
https://pypi.org/project/Flask-Login/
`pip install bcrypt` - used to hash passwords
https://pypi.org/project/bcrypt/


**Register**
Implement `UserRegistrationForm`.


Use of javascripts for validators.

errors encountered: Some special characters were not included at the first iteration of validators. Making any password like `mypassword!1` invalide.

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
        
        company_name = StringField("Enter your company name", validators=[Length(max=200)], render_kw={"placeholder": "Company Name"})
        user_type = SelectField("Select User Type", choices=[(UserType.GRANTEE.value, "Grantee"), (UserType.GRANTER.value, "Granter")], validators=[DataRequired()])
        submit = SubmitField("Register")

        def validate_username(self, username):
            existing_user_username = User.query.filter_by(username=username.data).first()
            if existing_user_username:
                raise ValidationError("This username is already used")


Also added checks in function to username or email address is already used, to avoid 500 error.

    if existing_user:
            flash('Username already exists.', 'danger')
            return render_template('register.html', form=form)

@login_required decorator

**Extends template**
Documentation : https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/

**Navbar**
Documentation
https://getbootstrap.com/docs/4.0/components/navbar/

**Error page handling**
For errors: 404 and 500 only

**WTF Forms**
    https://wtforms.readthedocs.io/en/3.1.x/
    https://flask.palletsprojects.com/en/3.0.x/patterns/wtforms/

    Mention use of validators to display messages when form is not compeleted

    Use of CSRF Token
    from flask_wtf.csrf import CSRFProtect
    import os
    from flask import flash (to display toast like messages)

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

Create .env file in root directory and the following line:
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



**User types**
`from enum import Enum`
https://docs.python.org/3/library/enum.html

**Foreign Keys**
FK problem
Note: in `class GrantAnswer(db.Model)` the foreign key applied to field `grant_question_id` is `grant_question.id`. It seems running `flask db migrate` autorenamed the table generated by `class GrantQuestion(db.Model)` to `grant_question. This was found out by checking migration file: #bdd8261021d8.




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

**To improve**
MIgrations : I made a few mistakes with the foreign keys, in particular when trying to establish relationships. I had to delete the migrations and restrat from strach on a few occasions, as I didnt know how to fix my problems from the migration files.