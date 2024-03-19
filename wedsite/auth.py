from flask import Blueprint, render_template, session, redirect, request, url_for
from .models import User
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template("login.html")





@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')

@auth.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

