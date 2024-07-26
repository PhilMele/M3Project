from flask import Flask, render_template

app = Flask(__name__)
app.run(debug=True)
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

# Granter Interface Logic

if __name__ == "__main__":
    app.run(debug=True)
