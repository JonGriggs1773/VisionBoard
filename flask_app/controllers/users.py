from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash
import pprint
import pickle

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
    
@app.route('/login', methods = ['POST'])
def login_user():
    if User.login_user(request.form):
        return redirect('/dashboard')
    else:
        return redirect('/login/page')

#! Add appropriate variables to dashboard
@app.route('/dashboard')
def render_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    else:
        print(session['user_id'])
        user = User.get_user_with_ltgs_by_user_id(session['user_id'])
        for ltg in user.long_term_goals:
            print("Look Here: ", ltg.image)
            #? Converting each image in ltg's from byte string to regualr string so the file can be read properly in the templates
            ltg.image = ltg.image.decode("utf-8")
            print("AFTER CHANGES: ", ltg.image)
        return render_template("dashboard.html", user = user)
    
@app.route('/logout')
def logout_user():
    session.clear()
    return redirect('/')