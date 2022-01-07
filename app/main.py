from flask import Flask, render_template, flash, request, url_for, redirect, session, jsonify


# GCP OpenID Connection Configuration
#GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
#GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
#GOOGLE_DISCOVERY_URL = (
#    "https://accounts.google.com/.well-known/openid-configuration"
#)

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/reports/')
def reports():
    return render_template("reports.html")

@app.route('/email_api/')
def email_api():
    return render_template("email_api.html")

@app.route('/security/')
def security():
    return render_template("security.html")

@app.route('/quick_links/')
def quick_links():
    return render_template("quick_links.html")

@app.route('/user_management/')
def user_management():
    return render_template("user_management.html")

@app.route('/add_user/')
def add_user():
    return render_template("add_user.html")

@app.route('/all_users/')
def all_users():
    return render_template("all_users.html")

@app.route('/audit_user/')
def audit_user():
    return render_template("audit_user.html")

@app.route('/system_status/')
def audit_user():
    return render_template("system_status.html")

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
