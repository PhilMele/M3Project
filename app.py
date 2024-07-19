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
@app.route("/dashboard")
def dashboard():
    return render_template('grantee/grantee-dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
