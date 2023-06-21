from flask_app import app
from flask_app.models.long_term_goal import LTG
from flask_app.models.user import User
from flask import render_template, redirect, request, session


@app.route('/ltg/form')
def render_ltg_form():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template('addLTG.html', user = User.get_user_by_id(session['user_id']))
    
@app.route('/ltg/submit', methods = ['POST'])
def create_ltg():
    if LTG.create_long_term_goal(request.form):
        return redirect('/dashboard')
    else:
        return redirect('/ltg/form')
