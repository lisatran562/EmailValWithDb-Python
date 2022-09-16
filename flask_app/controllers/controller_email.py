from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.model_email import Email


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if not Email.validate(request.form):
        return redirect('/')
        
    Email.create_one(request.form)
    return redirect('/success')



@app.route('/success')
def display_success():
    all_emails = Email.get_all()
    print(all_emails)
    
    if all_emails == None:
        return redirect('/')

    return render_template('success.html', all_emails=all_emails)