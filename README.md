# M3Project - Grant Management

![rendering](/documentation/screen-shots/front-page/front-page.png)


View the live site: <a href="https://grant-management-mp3-709b64ecedb2.herokuapp.com/" target="_blank">Click Here</a>

# Table of Contents

1. [User Experience](#ux)
   - [Project Goals](#project-goals)
   - [User Stories](#ux-subsection)
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
   - [CSRF Token & WTForms](#csrf-token)
   - [Context Processor & Navbar](#context-processor)
   - [Template Filter & Currency Display](#currency-display)
   - [Decorators](#decorators)
   - [Customer Error Pages](#error-pages)
4. [Technologies](#tech)
5. [Testing](#testing)
   - [Validator Testing](#val-testing)
     * [HTML](#html)
     * [CSS](#css)
     * [Javascript](#js)
     * [Python](#py)
   - [Lighthouse Testing](#lighthouse-testing)
   - [User Testing](#user-testing)
6. [Bugs](#bugs)
   - [Current bugs](#current-bugs)
   - [Design & User Experience improvements](#design-improvements)
   - [Logic improvements & Backend](#logic-improvements)    
7. [Deployment](#deployment)
   - [Local Deployment](#local-deployment)
   - [Heroku Deployment](#heroku-deployment)
8. [Credits](#credits)


## 1. User Experience <a name="ux"></a>

There are three types of users for this product. The actual user applying looking to apply for a grant (the "Grantee"), the user issuing and validating granter applications (the "Granter") and the administrator.

### 1.1 Project Goals <a name="project-goals"></a>

The goal of this product is to offer a platform to people to apply for grant with local authorities. 

This is platform is not meant to be standalone website, but instead will be linked to an existing website. By clicking on a link on the local authorities website, the user will be redirected to the index page. As a result, there is not need for additional page for the unauthenticated user than the login and account registration page.

With the exception of large granting bodies, grants are still applied to by email. 

This makes it hard for grantees to know what is available, and also harder for granters who still need to look into their emails to find applications: this causes a second problem around document control.

The whole grant validation and management process is a very long process, which could be split into 2 mains phases:
* Phase 1 - Grant creation and grant application. This phase includes the creation and the publication of the grant, by the Granter, and the application phase by the Grantee all the way to grant validation or rejection by the Granter.
* Phase 2 - Grant Management. This phase includes the management of reporting documentation from both parties together with communication.

Note: Although it was my intention to cover both phases in this project, I have come to realise, Phase 1 was already a longer piece than anticipated. As a result, this product will address Phase 1 only.

### 1.2 User Stories <a name="user-goals"></a>

* As a user (granter, admin or grantee) I want to be able to create an account.

* As the administrator I want to assign a Granter role to accounts registered as Grantee as default.

* As a granter, I want all people accessing my grants to be logged in, for analytics purposes. 

* As a grantee I want to be able to created an account and delete it.

* As a granter I want to keep track of any application submitted by my grantees, even if they delete an account, for KPI purposes.

* As a granter, I want to create a grant and attach any number of questions to it, edit or delete them.

* As an adminstrator, I do not want granter to be able to delete grant or questions after the grant is accessible to grantees.

* As the administrator I want to be able to link questions to grants and their issuing granter.

* As a granter, I want to be able to edit or delete questions.

* As a granter, I want to decide the grant status: whether it is innactive (not ready to be published), active (published) and close whenever my fund has run out (closed). 

* As a grantee, I want to be able to create an account and apply to any available grant.

* As a grantee, I want to be able to answer grant questions, edit or delete them

* As a grantee, before or after submitting my application I want to be able to review my application.

* As a granter, I do not want submitted application to be editable.

* As a granter, I do not want application to be submitted against grants with a status of "closed".

* As a granter, I want to be able to review application and either approve or reject the appplication.

* As a granter, I do not want to know the identity of the grantee when assessing their application.

* As a grantee, I want to be kept up to date of my application whether the application is still pending, approved or rejected. 



## 2. Design <a name="ui"></a>

The design is simple and avoids using images.

It is made to work on screen width from 340px to 4K, but the content width is capped to 840pxs.

### 2.1 Colours <a name="colours"></a>
As this is a coprorate product, colours used are simple, but also add some sense excitment through bright yellow and orange.

![Colour Palette](documentation/colour-palette/colour-palette.png)

### 2.2 Typography <a name="typography"></a>
Typography follows the same principle as the colours with the use of Poppins and Nerko One.

We have selected Google Fonts, instead of custom fonts, to benefit from better support.

This font can be found on: https://fonts.google.com/

### 2.3 Icons & Images <a name="icons-images"></a>

No static images were used for this project, except for the favicon.

Credits need to however be given to Fontawesome for their icons: https://fontawesome.com/

### 2.4 Wireframes <a name="wireframes"></a>

<details>
    <summary>Login</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/login.png" alt="login wireframe page"  width="320px" />
    </p>
</details>

<details>
    <summary>Register</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/register.png" alt="register wireframe page"  width="320px" />
    </p>
</details>

<details>
    <summary>Grantee Dashboard</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/grantee-dashboard.png" alt="grantee-dashboard wireframe page"  width="320px"/>
    </p>
</details>

<details>
    <summary>Grants Available</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/grants-available.png" alt="grants-available wireframe page"  width="320px" />
    </p>
</details>

<details>
    <summary>Apply to Grant</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/apply-to-grant.png" alt="apply-to-grant wireframe page"  width="320px" />
    </p>
</details>

<details>
    <summary>Granter Dashboard</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/granter-dashboard.png" alt="granter-dashboard wireframe page"  width="320px"/>
    </p>
</details>

<details>
    <summary>Create Grant</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/create-new-grant.png" alt="create-new-grant wireframe page"  width="320px"/>
    </p>
</details>

<details>
    <summary>Show Grant</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/show-grant.png" alt="show-grant wireframe page"  width="320px"/>
    </p>
</details>

<details>
    <summary>Show All Grant Applications</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/show-all-grant-application.png" alt="show-all-grant-application wireframe page"  width="320px" />
    </p>
</details>

<details>
    <summary>Show User Grant Applications</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/show-user-grant-application.png" alt="show-user-grant-application wireframe page"  width="320px" />
    </p>
</details>

<details>
    <summary>Account</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/account.png" alt="account wireframe page"  width="320px" />
    </p>
</details>

<details>
    <summary>Wireframe interactions</summary>
    <p>
        <img src="/documentation/screen-shots/wireframes/wireframes-interactions.png" alt="wireframes interactions wireframe page"  width="320px" />
    </p>
</details>


### 2.5 Databases <a name="databases"></a>

**Setup - SQLAlchemy**

To setup the database, the following steps need to be taken:
* To get started run: `pip install flask-sqlalchemy` (Documentation: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
* To make changes to database install Flask-Migrate package and run : `pip install Flask-Migrate` (Documentation:https://flask-migrate.readthedocs.io/en/latest/)
* An initial migration will need to be made by running command : `$ flask db init`. (db refers to the database)
* Everytime a change is made to the models run commands :`$ flask db migrate -m "migration description"` & `$ flask db upgrade`

**app.py** should look like this:

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_dev_key')

    # Database
    load_dotenv()  # take environment variables from .env.

    # Fix for heroku database noted as "postgres" intsead of "postgresql"
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    db = SQLAlchemy(app)
    bcrypt = Bcrypt(app)

    # Flask-Migrate
    migrate = Migrate(app, db)

Note: some of this code involves the use of Heroku for deployment, which is covered at the end of this Readme.


**Problem encountered**: In `app.config['SQLALCHEMY_DATABASE_URI'] =`, I had to specify the full path as the local project was hosted on OneDrive and caused problems. If the project was hosted directly on local machine, the use of the relative path should work.

**Setup - PostgreSQL**

Instal postgres on local: https://www.postgresql.org/download/

Normal practice:
* To set up of PostGres on Local run : `pip install psycopg2` (Documentation: https://medium.com/@shahrukhshl0/building-a-flask-crud-application-with-psycopg2-58de201e3c14)

Issues encountered and solution:
* This may have been specific to my local setup, but I had to use : `pip install psycopg2-binary` (Documentation: https://pypi.org/project/psycopg2-binary/). My requirements.txt file lists : `psycopg2-binary==2.9.9`

**Create environement variables & Setup PostgreSQL on local**

To avoid passwords and secret keys being leaked on github when the code is pushed, we use variables stored in files that are not pushed to git hub. (Documentation: https://pypi.org/project/python-dotenv/)

To do this run: `pip install python-dotenv`

To app.py, add:

    ...
    from dotenv import load_dotenv
    ...
    load_dotenv()
    ...
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

After this, create `.env` file in root directory and the following line:
`DATABASE_URL=postgresql://[username]:[postgres-password]@localhost/[databasename]`

**Problem encountered**: note the change for `database_url`. This is due to a problem faced during the deployment on Heroku returning the following message: `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres`

This error is due to a change in SQLalchemy library which has not been reflected with Heroku. The library now requires a reference to `postgresql` which Heroku still refers as `postgres`.

As a result, in order for the library to work on heroku an if statement has been added to the code, which handles this situation.

Another solution could have been to roll the library back to a version prior to <1.4.0 (1.3.23 is the last 1.3.x release).

Credit for solution: https://stackoverflow.com/questions/66690321/flask-and-heroku-sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy

**Model Overview**

The models define the structure and relationships of entities in the application. 

These entities include users, grants, grant applications, questions related to grants, and answers to those questions. 

Each model corresponds to a table in a PostgreSQL database.

**ER Diagram**

<img src="documentation/erd/flask - ERD.png" alt="" width="320px">

UserType is an enumeration used to distinguish between the two user types: "Grantee" and "Granter".

This enum is associated with the user_type field in the User model to indicate the type of user, leading to specific permissions in the business logic.

**1. User Model**

Represents the users of the system: Grantees and Granters.

| **Field**       | **Description**                                              |
|-----------------|--------------------------------------------------------------|
| `id`            | Primary key, unique identifier for each user.                |
| `username`      | Unique username of the user.                                 |
| `password`      | User's password (likely stored hashed).                      |
| `email`         | Unique email of the user.                                    |
| `company_name`  | Company name (optional).                                     |
| `user_type`     | Either "Grantee" or "Granter" as per the `UserType` enum.    |
| `created_on`    | Timestamp of when the user was created.                      |

Relationships:
* Grants: A User (acting as a granter) can have many grants associated with them (usergrants).
* GrantApplications: A User (acting as a grantee) can submit multiple grant applications (usergrantapplications).
* GrantAnswers: A User can submit multiple answers to grant questions (usergrantanswers).

**UserType Enum**

UserType is an enumeration used to distinguish between the two user types: "Grantee" and "Granter".

This enum is associated with the user_type field in the User model to indicate the type of user, leading to specific permissions in the business logic.

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
    


**2. Grant Model**

Represents a grant that is available for applicants to apply for.

| **Field**           | **Description**                                                 |
|---------------------|-----------------------------------------------------------------|
| `id`                | Primary key, unique identifier for each grant.                  |
| `user_id`           | Foreign key linking to the User object who created the grant. |
| `grant_title`       | Title of the grant.                                             |
| `grant_description` | Description of the grant.                                       |
| `grant_fund`        | Amount of funds available for the grant.                        |
| `created_on`        | Timestamp of when the grant was created.                        |
| `is_active`         | Indicates if the grant is currently active.                     |
| `is_closed`         | Indicates if the grant is closed for applications.              |


Relationships:
* User: The Grant model has a foreign key relationship with User (granter).
* GrantQuestions: A grant can have multiple questions (questions) linked to it.
* GrantApplications: A grant can have multiple applications (applications) linked to it.

**3. GrantQuestion Model**

Represents a question associated with a grant that applicants need to answer.

| **Field**     | **Description**                                                      |
|---------------|----------------------------------------------------------------------|
| `id`          | Primary key, unique identifier for each question.                    |
| `user_id`     | Foreign key linking to the User object who created the question (granter).   |
| `grant_id`    | Foreign key linking to the Grant object the question is associated with.     |
| `question`    | The actual question text.                                            |
| `created_on`  | Timestamp of when the question was created.                          |


Relationships:
* Grant: A question belongs to a specific grant (grant).
* GrantAnswers: A question can have multiple answers (answers) submitted by applicants.

**4. GrantApplication Model**

Represents an application that a user (grantee) submits for a grant.

| **Field**       | **Description**                                                        |
|-----------------|------------------------------------------------------------------------|
| `id`            | Primary key, unique identifier for each application.                   |
| `user_id`       | Foreign key linking to the User object who submitted the application (grantee).|
| `grant_id`      | Foreign key linking to the Grant object the application is for.               |
| `is_submitted`  | Boolean indicating if the application has been submitted.              |
| `is_approved`   | Boolean indicating if the application has been approved.               |
| `is_rejected`   | Boolean indicating if the application has been rejected.               |


Relationships:
* Grant: The application is linked to a specific grant id.
* User: The application is submitted by a specific user id.
* GrantAnswers: An application can have multiple answers submitted by a User.

**5. GrantAnswer Model**

Represents an answer to a question in a grant application.

| **Field**          | **Description**                                                       |
|--------------------|-----------------------------------------------------------------------|
| `id`               | Primary key, unique identifier for each answer.                       |
| `user_id`          | Foreign key linking to the User object who submitted the answer.             |
| `application_id`   | Foreign key linking to the GrantApplication object the answer is attached to.|
| `grant_question_id`| Foreign key linking to the GrantQuestion object being answered.              |
| `answer`           | The actual answer text.                                               |
| `created_on`       | Timestamp of when the answer was created.                             |

Relationships:
* User: The answer is submitted by a specific user.
* GrantApplication: The answer belongs to a specific application.
* GrantQuestion: The answer is associated with a specific question.

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

This panel was solely built for the purpose of the assessment of the project to give assor easy access to both user types.

**Note**: An alternative to the admin panel could have been a superuser system, where the Granter role would be assigned through command-line commands. However, since the assessment will be conducted via Heroku, where the command line is not accessible to the assessor, this solution would not have been practical.

As the project will be accessible on github, the admin panel does not allow for user account deletion, to avoid outside user deleting all users from the admin panel.

To delete a user account, one need to log-in with the user credentials and find the "delete" option in Account Details section in Navbar.

As part future development, it would make sense to build a superuser function and have a django style admin panel.

To access admin panel simply follow these steps:
* Register an account
* To the root url add `admin`. (for example: http://127.0.0.1:5500/admin)

You will be prompted to the admin page where for each user, `current_user` can see their user type in the middle column and the possibility to switch to another user type in the right column.

By clicking on the other user type in the right column, the related user account will change from one type to the other. 

<img src="documentation/screen-shots/website-screenshots/admin-panel.png" alt="change user type in admin panel" width="320px">


### 3.3 Create Grant <a name="create-grant"></a>
This functionnality is only available to Granter and is triggered by `create_new_grant().

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

<img src="documentation/screen-shots/website-screenshots/show-grant.png" alt="display specific grant management page to granter" width="320px">

**Note on problem encountered**: the fund field of the Grant Model is an interger. As interger have a range limit of -2,147,483,648 to 2,147,483,647, all grant value exceeding this range would generate a error.

As a result, a validator was added to the form to check the validity of the value entered by the granter. This validator takes the form of a javascript in `script.js` file.

### 3.5 Read, Edit & Delete Grant Questions <a name="read-edit-delete-grant-questions"></a>

This functionnality is only available to Granter and is also managed by `show_grant()`, which takes the newly created `grant_id` as a parameter.

    def show_grant(grant_id):

This function also displays the possibility for the granter to read the grant and the questions they attached to it.

Questions are listed on the template through `list_question` variable, which returns all GrantQuestion objects in the database that match the filter of `grant_id` parameter.

    list_question = GrantQuestion.query.filter_by(grant_id=grant.id).order_by(GrantQuestion.id).all()

Question can be edited (through `edit_show_grant_question()`) or deleted (`delete_show_grant_question()`). The functions are linked within the template itself


    {%for question in list_question%}

    <div class="row mb-2 center-text">
        <div class="col-6">
            <a class="btn btn-primary btn-sm large-screen-width" href="{{ url_for('edit_show_grant_question', grant_id=grant.id, grantquestion_id=question.id) }}">Edit</a>
        </div>
        
        <div class="col-6">
            <a class="btn btn-danger btn-sm large-screen-width" href="{{ url_for('delete_show_grant_question', grant_id=grant.id, grantquestion_id=question.id) }}">Delete</a>
        </div>
    </div>

    {%endfor%}

Finally, Granter can manage the grant lifecycle from this page.  They can see the current status of the grant (inactive, active or closed), and change this status to the next one with `activate_grant()` and `close_grant()`. Grant objects are created are innactive by default (`is_active = False`)

    <div class="row mb-2 d-flex justify-content-center align-items-center">
        <div class="col-6">
            Click to switch status to:
        </div>
        
        <div class="col-6 d-flex justify-content-center align-items-center">
            {%if grant.is_active%}
            <a href="{{ url_for('close_grant', grant_id=grant.id)}}" class="btn btn-danger btn-sm large-screen-width">Close</a>
            {%else%}
            <a href="{{ url_for('activate_grant', grant_id=grant.id)}}" class="btn btn-success btn-sm large-screen-width">Activate</a>
        
            {%endif%}
        </div>
    </div>

Note: Once a grant is moved from inactive to active, the granter cannot de-activate it and can only close it. Same apply for deletion: Granter can only delete applications as long as the application is inactive.

Once closed, the grant can only be re-activated.

### 3.6 Create Grant Application <a name="create-application"></a>
This function is for Grantees to apply to a grant and is managed by `apply_to_grant()`, which takes the parameters of `grant_id` and `grant_application_id`.

This function is accessible directly from the Grantee Dashboard (`grantee-dashboard.html`) which redirects the user to `grants-available.html` template, managed by `grant_available()`.

`grant_available()` lists all active grants created by granters:

    grants = Grant.query.filter_by(is_active=True)

It also, lists all grants that the currently authenticated user (`current_user`) has started or even submitted, to avoid them submitting multiple similar application, or simply allowing them to start an application and finish later.

To do this, an additional variable was created `existing_applications`, which filters all applications made by current user.

    existing_applications = GrantApplication.query.filter_by(user_id=current_user.id).all()

As advised by my mentor Gareth McGirr, using a Dictionnary Comprehension, I can create a dictionnary and append an existing application (if it exists) against a grant_id by current_user.

The clearest definition I found is the following (form:https://www.datacamp.com/tutorial/python-dictionary-comprehension ):"Dictionary comprehension is a method for transforming one dictionary into another dictionary. During this transformation, items within the original dictionary can be conditionally included in the new dictionary, and each item can be transformed as needed."

    `dict_variable = {key:value for (key,value) in dictonary.items()}`

In practice, by passing `existing_applications` and `grants` in the template, the rendering of the list of grants and their existing applications from current_users was handled this way:

    {% for grant in grants %}     
        <!-- If application exists -->
            <!-- If application exists AND is submitted -->
            {% if grant.id in existing_application_id and existing_application_id[grant.id].is_submitted %}
            <div class="col-4 d-flex justify-content-center btn-sm large-screen-width">
                <a href="{{ url_for('read_submitted_application', grant_id=grant.id, grant_application_id=existing_application_id[grant.id].id) }}" class="btn btn-primary btn-sm">Open</a>
            </div>
            <!-- If application exists AND is NOT submitted -->
            {% elif grant.id in existing_application_id and not existing_application_id[grant.id].is_submitted %}
            <div class="col-4 d-flex justify-content-center btn-sm large-screen-width">
                <a href="{{ url_for('apply_to_grant', grant_id=grant.id, grant_application_id=existing_application_id[grant.id].id) }}" class="btn btn-primary btn-sm">Open</a>
            </div>
        <!-- If application does not exist -->
        {%else%}
            <div class="col-4 d-flex justify-content-center btn-sm large-screen-width">
                <a href="{{ url_for('activate_application', grant_id=grant.id) }}" class="btn btn-primary btn-sm">Apply</a>
            </div>
        {%endif%}
    {% endfor %}

Once grants with an existing application and those without one are identified, `current_user` can either :
* Create a new application through `activate_application()` which will create an new application model object and redirect the user to `apply_to_grant()` with the parameters of the current `grand_id` and the newly created `grant_application_id`.
* Continue the existing application or read an a already submitted application. This part is covered in the next section.

### 3.7 Read, Edit & Delete Application <a name="read-edit-delete-application"></a>
This section distinguishes whether the application has been submitted by the user or not.


<img src="documentation/screen-shots/website-screenshots/submit-application.png" alt="submit grant application" width="320px">


**Application Not Submitted**

Application that are not submitted are managed by `apply_to_grant()` which allows the grantee to either:
* Answer unanswered questions using `AnswerGrantQuestionForm()` through variable `grantanswerform`
* Edit previously answered questions through the same `AnswerGrantQuestionForm()` using form variable `editanswerform` which redirects the user to `edit_grant_answer()`
* Delete answered questions or delete the application as a whole through redirecting user to `delete_grant_answer()`

This function returns:
* All GrantQuestion objects attached to the `grant_id` parameter and 
* All GrantAnswer objects that have been created against the same `grant_id` parameter by `current_user`.

Similarly to the previous section, it uses `Dictionnary Comprehension` to achieve the combination of these two points.

**Note for future improvements**: the code could be simplified. At the time of creating `apply_to_grant()`, `grant_application_id` wasnt passed as a parameter of the function and was added later on. The code could make the Dictionnary Comprehension redundant by simply taking into account `grant_application_id` in the filter of the variable that returns the GrantAnswer objects.

Finally, some javascript at the bottom of template regulates whether the grantee can submit their application or not, by checking if all questions have been answered.

If all questions are answered (`submit_button = True`) then submit button becomes clickable, otherwise it shows that the application is not completed.

Business logic (python):

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

Rendering logic (html + JS):

    {%if submit_button == True %}
        <a href="{{ url_for('submit_application', grant_id=grant.id, grant_application_id=grant_application_id) }}" class="btn btn-success btn-sm large-screen-width">Submit</a>
        {%else%}
        <a href="" class="btn btn-secondary btn-sm large-screen-width">Application Incomplete</a>
    {%endif%}

    <script>
        function toggleEditForm(questionId) {
            var form = document.getElementById('edit-form-' + questionId);
            if (form.style.display === 'none' || form.style.display === '') {
                form.style.display = 'block';
            } else {
                form.style.display = 'none';
            }
        }
    </script>


**Application Submitted**

Once submitted, the Grantee is redirected to `read-submitted-application.html` and can only read or delete their application.

This template is managed by `read_submitted_application()`. The function returns all questions listed against `grant_id` parameter, then creates a python list of matching GrantAnswer objects through a loop.

The loop returns GrantAnswer objects that with a common `current_user.id` and `grant_question.id`.

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

Grantee can then follow the status of their application on the dashboard from submitted, rejected or approved.

### 3.8 Submit Application <a name="submit-application"></a>
Application submission is managed by `submit_application()` and takes the parameters of `grant_application_id` and `grant_id` and redirects the user to `read_submitted_application()`and its related template.

In order to avoid users submitting other users proposals by playing with the URL, the function includes a check before marking the application_id as submitted:

    if submitted_application_user_id == current_user.id:
        application.is_submitted = True

This check ensures that the submitting user is the user that has created the proposal in the first instance.

### 3.9 Approve & Reject Application <a name="approve-reject-application"></a>
Approving and rejecting application is only available to Granter.

Grantees applications can be accessed from the Granter Dashboard, by clicking on "Application", which redirecs the granter to `show_all_grant_application()` passing `grant_id` as a parameter.

This function returns all applications sharing a common `grant_id` foreign key. In addition, it filters application that have a User set as None.

This scenario could happen, as a user might submit an application but decides to delete their account.

There is a case for the granting authority wanting to keep track of these applications for KPI pespectives. As a result, they are not deleted if the submitting user deletes their account. They were however removed from display, as there is no current use for the project at this stage.

    applications = (GrantApplication.query.filter_by(grant_id=grant_id, is_submitted = True)).filter(GrantApplication.user_id.isnot(None)).all()

**Note for future improvements**: in order to implement the KPI element mentioned above, it would make sense to keep the user ID assigned to the application, and not delete the user model object when the user decides to delete their account and simply remove personal information covered by GDPR. 

When accessing the applications, the granter can click on each of them to review them and switch each application status to either "Approved" (`approve_user_grant_application_id()`)  or "Rejected" (`reject_user_grant_application_id()`)

<img src="documentation/screen-shots/website-screenshots/approve-reject-application.png" alt="approve or reject grant application" width="320px">

Grantee can then see the status of their application changed from their dashboard.

<img src="documentation/screen-shots/website-screenshots/grantee-dashboard.png" alt="grantee dashboard view with application status" width="320px">

### 3.10 CSRF Token & WTForms <a name="csrf-token"></a>
The projects introduces the use of WTForms and CSRF Token, for increased security.

To get the package working, 2 dependencies will need to be installed: 

    pip install wtforms
    pip install flask-wtf

Once installed, at the top of app.py template, import the followings:

    from wtforms.form import Form
    from flask_wtf import FlaskForm
    from wtforms import BooleanField, StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField
    from wtforms.validators import DataRequired, InputRequired, Length, ValidationError,Regexp


WTForms allows to create forms with backend validators easily.

In this project, the forms also include the use of CSRF token for increased security.

    from flask_wtf.csrf import CSRFProtect
    import os
    from flask import flash 

    #CSRF Token
    csrf = CSRFProtect(app) 


Taking a short example with the UserLoginForm used for user authentication:

    class UserLoginForm(FlaskForm):
        username = StringField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Username"})
        password = PasswordField(validators=[DataRequired(), Length(min=4, max=200)], render_kw={"placeholder": "Password"})
        submit = SubmitField("Login")

The form here checks the data entered in not missing (`DataRequired()`), constrain the length of each field (`Length(min=4, max=200)]`) and adds a placeholder (`render_kw={"placeholder": "Username"}`)


The form is then used in the business logic as follows:

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

Finally, in the template renders the form in the classic format, with the addition of the CSRF token:

    <form method="POST" class="auth-form-container">
        {{ form.csrf_token(id = "unique_id") }}
        {{ form.hidden_tag() }}

        <div class="row mb-3">
            <div class="col">
                {{ form.username(class="form-control") }}
            </div>
        </div>

        <div class="row mb-3">
            <div class="col">
                {{ form.password(class="form-control") }}
            </div>
        </div>

        <div class="row">
            <div class="col center-text">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </div>
    </form>

**First problem encountered during the set up of the CSRF token**: During the original setup, the CSRF token was generated through `app.config['SECRET_KEY'] = os.urandom(24).hex()`, as seen on some documentation. Although this appraoch worked in local, it did not work in Heroku.

To solve this problem, I had to generate a unique token and add it to Heroku's envorionment variables.

Changing the initial key generating line to : 

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_dev_key')

To generate this unique token I used the following link: https://djecrety.ir/


**Second problem encountered during the set up of the CSRF token**: The CSRF documentaton recommends to call the token in the form this way `{{ form.csrf_token }}`. 

However, this produced the following warning the browser: `[DOM] Found 2 elements with non-unique id #csrf_token`.

Changing to `{{form.csrf_token()}}` solved this problem. This explains the `{{ form.csrf_token(id = "unique_id") }}` tag on index.html.

Useful links:
* Documentation: https://wtforms.readthedocs.io/en/3.1.x/
* Documentation: https://flask.palletsprojects.com/en/3.0.x/patterns/wtforms/
* Documentation to set up CSRF Token : https://flask-wtf.readthedocs.io/en/0.15.x/csrf/
* Additional Credits to set up CSRF Token : https://stackoverflow.com/questions/34902378/where-do-i-get-secret-key-for-flask
* Found 2 elements with non-unique id #csrf_token: https://www.reddit.com/r/flask/comments/gtjwbt/two_forms_csrf_token_nonunique_id_chrome_warning/

### 3.11 Context Processor & Navbar <a name="context-processor"></a>

The project includes a boostrap navbar and displays 2 different versions based on the UserType.

**Problem encountered**: The initial logic `  {% if current_user.user_type == UserType.GRANTEE %}` wasnt sufficent to make `UserType` from the User Model available in the `if statement`.

In order to make UserType available, a `context processor` had to be injected which can be found in the template as follows:

    @app.context_processor
    def inject_user_type():
        return dict(UserType=UserType)

The logic `{% if current_user.user_type == UserType.GRANTEE %}` in the template now works.

Useful Link:
* Documentation: https://flask.palletsprojects.com/en/2.3.x/templating/

### 3.12 Template Filter & Currency Display <a name="currency-display"></a>
To display currency with a Pound sign, a seperate function had to be implemented in app.py: 

    @app.template_filter('currency')
    def currency_filter(value):
        try:
            return f"£ {value:,.2f}"
        except (ValueError, TypeError):
            return value

Once implemented, the template filter can be called (in £, only)  by adding a `| currency`:

    {{ grantapplication.grant.grant_fund | currency }}

Useful Links:
* Doucmentation: https://flask.palletsprojects.com/en/1.1.x/templating/
* Additional help: https://stackoverflow.com/questions/12078571/jinja-templates-format-a-float-as-comma-separated-currency

### 3.13 Decorators <a name="decorators"></a>

The project introduces `@login_required` decorator, which allows to only allow authenticated users to access a specific page.

The decorator is used on function, with the exception of `index()` (login function) and `register()` (user registration function).

To implement it import login required at the top of app.py:

    from flask_login import login_required

Then call the decorator on top of each function:

    @login_required
    def admin():

### 3.14 Customer Error Pages <a name="error-pages"></a>

To improve the user experience in the unfortunate event of a internal server error (500) or missing page (404) bespoke error handling templates have been created, which can be found at the following paths:
* `templates\error-handling\404.html`
* `templates\error-handling\500.html`

## 4. Technologies <a name="tech"></a>
* HTML & CSS - Used for front end rendering on templates.
* Bootstrap - The Bootstrap framework is used throughout this website for layouts and styling.
* Javascript - Used on a few occasions for rendering purposes.
* Flask & Python - Use for business logic and backend
* Font Awesome - Font awesome Icons are used for the social icons displayed in the footer and the navbar's "burger menu" in mobile view.
* Google Fonts - Google fonts are used to render the fonts.
* Visual Studio Code - VS Code is the Integrated Development Environment used to develop the Website.
* GitHub - GithHub is the hosting site used to store the source code for the Website and Git Pages is used for the deployment of the live site.
* Git - Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* Google Chrome Developer Tools - Used to debug front end.
* Pixso - Used to design wireframes.
* ui.dev - Used to generate first image in Readme file rendering site in different format.
* notion.so - Used to generate tables for Readme file in markdown format.
* Heroku for server and PostgreSQL database hosting
* AWS S3 Bukect to host favicon
* DB Beaver for ERD generator

## 5. Testing <a name="testing"></a>
### 5.1 Validator Testing <a name="val-testing"></a>
#### 5.1.1 HTML <a name="html"></a>
   <details>
      <summary>index.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/index.png" alt="index.html" />
      </p>
   </details>

   <details>
      <summary>register.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/register.png" alt="register.html" />
      </p>
   </details>

   <details>
      <summary>account.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/account.png" alt="account.html" />
      </p>
   </details>

   <details>
      <summary>admin.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/admin.png" alt="admin.html" />
      </p>
   </details>

   <details>
      <summary>apply-to-grant.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/apply-to-grant.png" alt="apply-to-grant.html" />
      </p>
   </details>

   <details>
      <summary>grantee-dashboard.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/grantee-dashboard.png" alt="grantee-dashboard.html" />
      </p>
   </details>

   <details>
      <summary>grants-available.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/grants-available.png" alt="grants-available.html" />
      </p>
   </details>

   <details>
      <summary>read-submitted-application.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/read-submitted-application.png" alt="read-submitted-application.html" />
      </p>
   </details>

   <details>
      <summary>create-new-grant.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/create-new-grant.png" alt="create-new-grant.html" />
      </p>
   </details>

   <details>
      <summary>edit-question.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/edit-question.png" alt="edit-question.html" />
      </p>
   </details>

   <details>
      <summary>granter-dashboard.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/granter-dashboard.png" alt="granter-dashboard.html" />
      </p>
   </details>

   <details>
      <summary>show-all-grant-application.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/show-all-grant-application.png" alt="show-all-grant-application.html" />
      </p>
   </details>

   <details>
      <summary>show-grant.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/show-grant.png" alt="show-grant.html" />
      </p>
   </details>

   <details>
      <summary>show-user-grant-application.html</summary>
      <p>
         <img src="documentation/screen-shots/html-validators/show-user-grant-application.png" alt="show-user-grant-application.html" />
      </p>
   </details>

#### 5.1.2 CSS <a name="css"></a>

   <details>
      <summary>style.css</summary>
      <p>
         <img src="documentation/screen-shots/css-testing/css-jigsaw-testing.png" alt="styles.css" />
      </p>
   </details>

#### 5.1.3 Javascript <a name="js"></a>

<details>
    <summary>script.js</summary>
    <p>
        <img src="documentation/screen-shots/js-testing/js-testing.png" alt="javascript testing" />
    </p>

Note 1: the checker advises that the function is never used. This is because the checker was only provided the javascript.

The reference to the function can be found in the form:   

    {{ form.password(class="form-control", id="password", onkeyup="validatePassword()") }}

    {{ form.confirm_password(class="form-control", id="confirm_password", onkeyup="validatePassword()") }}

Note 2 : the checker advises that the toggle is never used. This is because the checker was only provided the javascript.

The reference to the toggle can be found in the button:     

    <button class="btn btn-primary btn-sm w-100" onclick="toggleEditForm('{{ grantquestion.id }}')">Save</button>

</details>


#### 5.1.3 Python <a name="py"></a>

   <details>
      <summary>app.py</summary>
      <p>
         <img src="documentation/screen-shots/python-testing/python-testing.png" alt="app.py" />
      </p>
   </details>

### 5.2 Lighthouse Testing <a name="lighthouse-testing"></a>
<details>
    <summary>INDEX</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-index.png" alt="index mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-index.png" alt="index desktop" />
    </p>
</details>
<details>
    <summary>REGISTER</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-register.png" alt="register mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-register.png" alt="register desktop" />
    </p>
</details>
<details>
    <summary>ACCOUNT</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-account.png" alt="account mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-account.png" alt="account desktop" />
    </p>
</details>
<details>
    <summary>ADMIN</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-admin.png" alt="admin mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-admin.png" alt="admin desktop" />
    </p>
</details>
<details>
    <summary>APPLY TO GRANT</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-apply-to-grant.png" alt="apply-to-grant mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-apply-to-grant.png" alt="apply-to-grant desktop" />
    </p>
</details>
<details>
    <summary>GRANTEE DASHBOARD</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-grantee-dashboard.png" alt="grantee-dashboard mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-grantee-dashboard.png" alt="grantee-dashboard desktop" />
    </p>
</details>
<details>
    <summary>GRANTS AVAILABLE</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-grants-available.png" alt="grants-available mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-grants-available.png" alt="grants-available desktop" />
    </p>
</details>
<details>
    <summary>READ SUBMITTED APPLICATION</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-read-submitted-application.png" alt="read-submitted-application mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-read-submitted-application.png" alt="read-submitted-application desktop" />
    </p>
</details>
<details>
    <summary>CREATE NEW GRANT</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-create-new-grant.png" alt="create-new-grant mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-create-new-grant.png" alt="create-new-grant desktop" />
    </p>
</details>
<details>
    <summary>INDEX</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-index.png" alt="index mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-index.png" alt="index desktop" />
    </p>
</details>
<details>
    <summary>EDIT QUESTION</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-edit-question.png" alt="edit-question mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-edit-question.png" alt="edit-question desktop" />
    </p>
</details>
<details>
    <summary>GRANTER DASHBOARD</summary>
    <p>
        <h3>Mobile</h3>
        <img src="documentation/screen-shots/lighthouse-testing/mobile-granter-dashboard.png" alt="granter-dashboard mobile" />
    </p>
    <p>
        <h3>Desktop</h3>
        <img src="documentation/screen-shots/lighthouse-testing/desktop-granter-dashboard.png" alt="granter-dashboard desktop" />
    </p>
</details>
   
### 5.3 User Testing <a name="user-testing"></a>

Click on this link to see manual testing steps: [Manual Testing Guide](MANUAL_TESTING.md)

## 6. Bugs <a name="bugs"></a>
### 6.1 Current bugs <a name="current-bugs"></a>

After testing completion, there is currently no bug.

Although the CSRF token is implemented, I am not sure how to test if it works correclty.

There is however a flaws both in frontend and backend that could be improved.

### 6.2 Design & User Experience Improvements <a name="design-improvements"></a>
* **Back Button**: the current design displays a line of text offering the user to go back to previous page. This could be improved with a button.
* Code repetiton: There is a few repetition in the css file in particular .status-colour, as the attribute that changes is the color of each class.
* **Simplifying display** : with a growing list of grant, it will become harder and harder for a user to find the grant they are looking for. Adding filters and a fuzzy search sysem could help improve this situation. Adding pagination, would also help reducing the requirement for performance by limiting the number of objects displayed. Finally The current design does not take advantage of wider screen: instead of having a single grant per row, a different display system could be implemented to show two grants per row in larger screens.
* **Add grant management & messaging system**: As part of the wireframe, a grant management system was planned to be implemented. One of the biggest issue with public grant is that all communications are done by email making document control very difficult. The platform could integrate a messaging and document uploading system so everything can be found on a single platform.
* **Warning before deletion** : There is currently no way to confirm the user intention to delete an object. Building an extra check to collect user confirmation before deletion would certainly be a must.
* **Grantee view for granter**: The grantee dashboard is available to the granter by simply changing the url from `granter-dashboard` to `dashbaord`. However, it would make sense to create a small toggle in the navbar for the granter to have access to the Grantee interface.

### 6.3 Logic & Backend Improvements <a name="logic-improvements"></a>
* **Add Admin Panel + superuser system**: In order to make this a commercial product, the first focus will be to create an admin panel with a superuser system. It seems Flask has a few libraries for it, however Django would probably provide a quicker way to achieve it, together with an easier way to manage dependencies between models.
* **Answer submission system**: I do not like the user having to click "submit" to save their answers. In the future it would be better to implement an automatic save of inputs left by the user.
* **Authentication** : the current code does not allow for the user to edit their password or change their credientials. It would be best practice to allow for such a system.
* **Additional security**: The code contains a few checks that prevent a grantee to access a granter dashboard, or validate another grantee's application. However, there are still a number of loopholes in the code (for example a grantee can edit another grantees application by modifying the url): as a result, additional security and logical checks could be implemented to improve the integrity of the data entered by users.
* **SSL Certificate** : Surprisingly, the deployed version is accessible in https, even though the SSL certificate on Heroku has not been activated. SSL certificate is a paying feature on Heroku. To make this a commercial grade product, an SSL certificate will need to be implemented. 
* **Add email system and notifications**: When applications are rejected or approved, a system could be implemented for the user to recieve an email notification to let them know of their application status. This email system could also be used to send other transactional emails (account verification). Additionally, live notification could be pushed to the user during browsing either through http requests, or via a websocket system but will require to pay for Redis heroku extension.
* **Add grading system**: some grant organisation have grading system, which could be implemented on the granter side.
* **Add date fields to grant model**: some grant application require to be submitted within a specific timeframe. Future development could include this feature.
* **Serve static file on external cloud platform**: the only image currently used is a favicon. This favicon is hosted on an S3 Bucket, as building a document uploader felt like an overkill for a single static image. However, in future developments, in would make sense to integrate with webservice to serve media files, in particular if users were to be asked to upload their own documents like financial models or presentations.
* **Prevent user from deleting application but instead remove it from display**: I do not like the idea of removing data from database. My experience in grant is limited, however I could imagine local authorities wanting to keep as much data as possible, with exception of anything GDPR would ask to be deleted. As a result, it would be interesting to switch the delete from database functions to function that simply remove data from front end. 
* **Contact us for not logged in users**: There is currently no communication system available for user wanting to contact the administrator if they are struggling to connect. This feature was initially built in the previous commits, but removed it as I could not finish it.
* **Migrations** : I had to delete the database a few times when setting up relationships between tables, as struggled to fix the migrations from the migratons files. As a result, the migration files do not show the full story of the database developments.

## 7. Deployment <a name="deployment"></a>
### 7.1 Local Deployment <a name="local-deployment"></a>

**Project Creation**: The project starts by creating a folder from VS Code name M3Project.

Once the folder is created, click on folder to start from sratch.

**Local Deployment**: To copy this project, you can use git clone from your terminal.

Go to the terminal and input: git clone https://github.com/PhilMele/M3Project.git in the directory you wish to have the project folder in.

Using your code editor, such as VS Code, click on open folder and click on the newly created folder.

### 7.2 Heroku Deployment <a name="heroku-deployment"></a>
To setup Heroku: 
* Install Heroku commandline (CLI) (Documentation: https://devcenter.heroku.com/articles/heroku-cli), run: `pip install gunicorn` 
* Install PostGres: `pip install psycopg2` 
* Set up requirements.txt file and run  `pip freeze > requirements.txt`
* Create Procfile and run `echo web: gunicorn app:app > Procfile`
* Login into Heroku: run `heroku login` (you will need to have an existing account)
* Create projet on heroku: heroku create project-name

Heroku Migration: a migration will be needed to migrate to heroku from your local repository. Run: `heroku run flask db upgrade`

**Problem encountered**: the Procfile generated with command line from documentation `echo web: gunicorn app:app > Procfile` created an issue relating to encoding. The encoding defaulted to UTF-16 instead of UTF-8.

To solve this problem: create a new Procfile through a Notepad, selected encoding UTF-8 and called it Procfile.txt in the same location as the actual Procfile. I then deleted the previous Procfile and renamed Procfile.txt to Procfile.

Useful Link:
* Credits: https://stackoverflow.com/questions/19846342/unable-to-parse-procfile

**Developement & Production Environements Documentation**

To set up the app as development or production, the following code has been implemented in app.py: 

    import os 

    if os.environ.get('FLASK_ENV') == 'development': 
        app.config['DEBUG'] = True 
            print("Running in development mode") 
        else: 
        app.config['DEBUG'] = False 
            print("Running in production mode")

    if __name__ == "__main__":
        app.run(debug=app.config['DEBUG'])

**Development Variables**

In `.env` previsouly created add the following variables: 

    FLASK_ENV=development 
    FLASK_DEBUG=1

These variables are for development only.

**Production Variables**

To set up production on heroku, the following variables need to be added to Heroku variables.

These variables can be defined in settings in the heroku dashboard. (Look for Config Vars section) then add the following: 

    DATABASE_URL = herokuDefinedDatabaseURL
    FLASK_ENV = `production` 
    FLASK_DEBUG = `0`
    SECRET_KEY = yourSecretKey (this relates to the CSRF token key)

**How to check if the variables work**

To check if it works, when running the project on local (or development) the following messages will print on the console: 

    Running in development mode 

In heroku the following line will be printed in the logs: 

    Running in production mode

## 8. Credits <a name="credits"></a>

* DB Beaver for ERD generator : https://dbeaver.com/docs/dbeaver/ER-Diagrams/
* JS password validator : https://gist.github.com/frizbee/5318c77d2084fa75cd00ea131399581a
* Flask WTForms Part 1 : https://wtforms.readthedocs.io/en/3.1.x/
* Flask WTForms Part 2 : https://flask.palletsprojects.com/en/3.0.x/patterns/wtforms/
* CSRF Token setup : https://flask-wtf.readthedocs.io/en/0.15.x/csrf/
* Solution to `Found 2 elements with non-unique id #csrf_token`: https://www.reddit.com/r/flask/comments/gtjwbt/two_forms_csrf_token_nonunique_id_chrome_warning/
* Procfile encoding solution: https://stackoverflow.com/questions/19846342/unable-to-parse-procfile
* Postgres setup : https://medium.com/@shahrukhshl0/building-a-flask-crud-application-with-psycopg2-58de201e3c14
* Postgres envnrionement variables: https://pypi.org/project/python-dotenv/
* Solve Postgres and Flask compatbility: https://stackoverflow.com/questions/66690321/flask-and-heroku-sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy
* Currency display : https://stackoverflow.com/questions/12078571/jinja-templates-format-a-float-as-comma-separated-currency
* John Elder for his Flask Friday youtube videos
* Gareth McGirr (mentor) for the advice to look at Dictonnary Comprehension and general advice on user experience improvements.
