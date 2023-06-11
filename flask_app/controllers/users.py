from flask_app import app
from flask import render_template, redirect, request, session, flash

@app.route('/')
def register_page():
    return render_template("register.html")

@app.route('/login')
def login_page():
    return render_template("login.html")