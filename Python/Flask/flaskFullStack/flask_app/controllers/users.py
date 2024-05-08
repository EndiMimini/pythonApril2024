from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/')
def controller():
    return redirect('/register')


@app.route('/register')
def registerPage():
    return render_template('register.html')


@app.route('/register/user', methods = ['POST'])
def registerUser():
    data = {
        'username': request.form['username'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    User.createUser(data)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboardPage():
    users = User.getAllUsers()
    return render_template('dashboard.html', users=users)


@app.route('/profile/<int:id>')
def profile(id):
    data ={
        'id': id
    }
    user = User.get_user_by_id(data)
    return render_template('profile.html', user=user)



@app.route('/edit/user/<int:id>')
def editProfile(id):
    data ={
        'id': id
    }
    user = User.get_user_by_id(data)
    return render_template('editProfile.html', user=user)

@app.route('/update/user/<int:id>', methods = ['POST'])
def updateUser(id):
    data = {
        'id': id,
        'username': request.form['username'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    User.delete_user(data)
    return redirect(request.referrer)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')