from flask_app import app
from flask import render_template, redirect, session, request


@app.route('/users')
def users():
   
    if 'users' not in session:
        session['sss']= []
        session['test'] = []
    session['users'] = session['test']
    return render_template('users.html')

@app.route('/users/add')
def addUser():
    return render_template('createUser.html')


@app.route('/users/create', methods = ['POST'])
def createUser():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
    }
    session['users'].append(data)
    session['test'] = session['users']
    return redirect('/users')