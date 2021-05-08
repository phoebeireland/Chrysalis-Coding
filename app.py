import os
from os import path
from flask import Flask, render_template, redirect, url_for, flash, session

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config.update(
    SECRET_KEY = os.environ.get('SECRET_KEY')
)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP', '127.0.0.1'),
        port = os.environ.get('PORT', '5000'),
        debug=True
    )