from flask_app import app
from flask_app.models.long_term_goal import LTG
from flask_app.models.short_term_goal import STG
from flask_app.models.user import User
from flask import render_template, redirect, request, session


@app.route('/add_stg/<int:id>')
def add_stg_form(id):
    if 'user_id' in session:
        session['ltg_id'] = id
        ltg = LTG.get_ltg_by_id(id)
        user = User.get_user_by_id(session['user_id'])
        return render_template('addSTG.html', ltg = ltg, user = user)
    else:
        return redirect('/')
    
    
@app.route('/stg/submit', methods = ['POST'])
def submit_stg():
    
    
    if STG.create_short_term_goal(request.form):
        session.pop('ltg_id', None)
        return redirect('/dashboard')
    
    else:
        ltg_id = session['ltg_id']
        return redirect(f'/add_stg/{ltg_id}')