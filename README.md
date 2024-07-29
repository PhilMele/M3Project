# M3Project



Features
Login

Extends template
Documentation : https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/

Navbar
Documentation
https://getbootstrap.com/docs/4.0/components/navbar/

Error page handling
For errors: 404 and 500 only

WTF Forms
    https://wtforms.readthedocs.io/en/3.1.x/
    https://flask.palletsprojects.com/en/3.0.x/patterns/wtforms/

    Mention use of validators to display messages when form is not compeleted

    Use of CSRF Token
    from flask_wtf.csrf import CSRFProtect
    import os
    from flask import flash (to display toast like messages)

Data base
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




