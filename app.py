from datetime import date

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

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
        pass
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