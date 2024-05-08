from flask_app import app
from flask import render_template, redirect, session, request
from datetime import datetime
@app.route('/')
def index():
    return redirect('/dashboard')


@app.route('/dashboard')
def dashbboard():
    session.clear()
    return render_template('dashboard.html')



@app.route('/order', methods = ['POST'])
def order():
    session['name']= request.form['name']
    session['studentId']= request.form['studentId']
    session['strawberry']= request.form['strawberry']
    session['rapsberry']= request.form['rapsberry']
    session['apple']= request.form['apple']
    session['totalItems'] = int(request.form['strawberry'])+ int(request.form['rapsberry'])+ int(request.form['apple'])
    session['currentDateTime'] = datetime.now()
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('order.html')