from datetime import date

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from validator_collection import validators, checkers, errors

from helpers import check_password, login_required
from models import *


#Configure application
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///calendar.db"
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show calendar"""

    return render_template("index.html")


app.route("/change_password", methods=["GET", "POST"])
def change_password():
    """Change users password"""

    return render_template("change_password")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in user"""

    if request.method == "POST":

        # Check empty input
        if not request.form.get("email") or not request.form.get("password"):
            flash("Please provide email and password")
            return render_template("login.html")

        # Check email and password
        if (
            checkers.is_email(request.form.get("email"))
            and user := User.query.filter(User.email == request.form.get("email")).scalar
        ):
            if check_password_hash(user.hash, request.form.get("password")):
                return redirect("/")
        else:
            flash("Invalid email and/or password")
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log out user"""

    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    return render_template("register.html")