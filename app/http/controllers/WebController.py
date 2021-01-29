from flask import render_template


def index():
    return render_template('index.html')


def home():
    return render_template('home.html')
