  # Create a new instance of the Flask class called "app"
from flask_app import app

from flask import render_template, redirect


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def dashboard():
    name = 'Endi'
    students = [
        {
            'firstName': 'Endi',
            'lastName': 'Mimini'
        },
        {
            'firstName': 'Klea',
            'lastName': 'Manushi'
        },
        {
            'firstName': 'Flogert',
            'lastName': 'Ciku'
        }
        ]
    return render_template('dashboard.html', loggedUser=name, students = students)


@app.route('/profile/<int:id>')
def profile(id):
    students = [
            {
                'firstName': 'Endi',
                'lastName': 'Mimini'
            },
            {
                'firstName': 'Klea',
                'lastName': 'Manushi'
            },
            {
                'firstName': 'Flogert',
                'lastName': 'Ciku'
            }
        ]
    return render_template('profile.html' , user = students[id-1] )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')


@app.route('/login', methods = ['POST'])
def login():
    return redirect('/')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/hello/<int:name>')
def hello(name):
    return f'Hello {name}'

@app.route('/repeat/<int:numri>/<fjala>')
def greeting(numri, fjala):
    return render_template('testing.html', numri=numri, fjala=fjala)