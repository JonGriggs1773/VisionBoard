from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models.long_term_goal import LTG
from werkzeug.utils import secure_filename
from flask_app.models.user import User
from flask_app import app
import os

UPLOAD_FOLDER = 'flask_app/static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/ltg/form')
def render_ltg_form():
    if 'user_id' not in session:
        return redirect('/')
    else:
        return render_template('addLTG.html', user = User.get_user_by_id(session['user_id']))
    
@app.route('/ltg/submit', methods = ['POST'])
def create_ltg():
    print("Files: ", request.files, "Form: ", request.form)
    if 'image' not in request.files:
        flash('No file part')
        return redirect('/ltg/form')
    image = request.files['image']
    print(image)
    if image.filename == '':
        flash('No selected file')
        return redirect('/ltg/form')
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        print("Filename: ", filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    if LTG.create_long_term_goal(request.form, filename):
        return redirect('/dashboard')
    else:
        return redirect('/ltg/form')
    
@app.route('/view/ltg/<int:id>')
def view_one_ltg_page(id):
    ltg = LTG.get_ltg_by_id(id)
    return render_template('viewOneLTG.html', ltg=ltg)

@app.route('/delete/ltg/<int:id>')
def delete_ltg(id):
    LTG.delete_ltg_by_id(id)
    return redirect('/dashboard')
