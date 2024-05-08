from flask_app import app
from flask import render_template, redirect, session, request
import random
import datetime
@app.route('/')
def index():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'goldAmmount' not in session:
        session['goldAmmount']= 0
        session['activites'] = []
    return render_template('dashboard.html')


@app.route('/process_money', methods = ['POST'])
def process_money():
    type = request.form['type']
    if type == 'farm':
        myWinnings = random.randint(10,20) 
        aktiviteti = {
            'message': f'Earned {myWinnings} golds from the farm. ({datetime.datetime.now()})',
            'ammount': myWinnings
        } 
        session['activites'].append(aktiviteti)
    elif type=='cave':
        myWinnings = random.randint(5,10)
        aktiviteti = {
            'message': f'Earned {myWinnings} golds from the cave. ({datetime.datetime.now()})',
            'ammount': myWinnings
        } 
        session['activites'].append(aktiviteti)
    elif type=='house':
        myWinnings = random.randint(2,5)
        aktiviteti = {
            'message': f'Earned {myWinnings} golds from the house. ({datetime.datetime.now()})',
            'ammount': myWinnings
        } 
        session['activites'].append(aktiviteti)
    else:
        myWinnings = random.randint(-50,50)
        if myWinnings>=0:
            aktiviteti = {
                'message': f'Entered a casino and won {myWinnings} golds. ({datetime.datetime.now()})',
                'ammount': myWinnings
            } 
            session['activites'].append(aktiviteti)
        else:
            aktiviteti = {
                'message': f'Entered a casino and lost {myWinnings} golds. ({datetime.datetime.now()})',
                'ammount': myWinnings
            } 
            session['activites'].append(aktiviteti)
    
    session['goldAmmount'] += myWinnings
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')