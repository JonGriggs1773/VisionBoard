from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash

@app.route('/')
def register_page():
    return render_template('register.html')

@app.route('/login/page')
def login_page():
    return render_template('login.html')

@app.route('/confirm/register', methods = ['POST'])
def sumbit_registration():
    if User.create_user(request.form):
        return redirect('/dashboard')
    else:
        return redirect('/')
    
@app.route("/login", methods = ['POST'])
def login_user():
    if User.login_user(request.form):
        return redirect('/dashboard')
    else:
        return redirect('/login/page')

#! Add appropriate variables to dashboard
@app.route('/dashboard')
def render_dashboard():
    if 'user_id' not in session:
        return render_template("dashboard.html")
    else:
        return redirect('/')