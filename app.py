import os
from os import path
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from forms import LoginForm, RegisterForm, CreatePost, EditPost, DeletePost


if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config.update(
    MONGO_DB = os.environ.get('MONGO_DB'),
    MONGO_URI = os.environ.get('MONGO_URI'),
    SECRET_KEY = os.environ.get('SECRET_KEY')
)

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
users = mongo.db.users
posts = mongo.db.posts


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        found_username = users.find_one({
            'username': request.form['username']
        })

        if not found_username:
            hashed_pw = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            users.insert_one({
                'username': register_form.username.data,
                'password': hashed_pw
            })
            session['username'] = request.form.get('username')
            flash(f'Thank you for Registering. You are now signed in!', 'primary')
            return redirect(url_for('index'))
        else:
            flash(f'Duplicate account detected. Please try again!', 'danger')
            return redirest(url_for('register'))
    
    return render_template('register.html', title='Register', form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        found_username = users.find_one({
            'username': request.form['username']
        })

        if found_username:
            if bcrypt.check_password_hash(
                found_username['password'], request.form.get('password').encode('utf-8')):
                session['username'] = request.form.get('username')
                session['logged-in'] = True
                flash(f'You are now logged in.', 'primary')
                return redirect(url_for('index'))

        flash(f'Login details not found. Please try again', 'danger')
        return redirect(url_for('login'))

    return render_template('login.html', title='Login', form=login_form)


@app.route('/logout')
def logout():
    session.clear()
    flash(f'Thank you for inspiring Women in Tech. See you soon!', 'primary')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP', '127.0.0.1'),
        port = os.environ.get('PORT', '5000'),
        debug=True
    )