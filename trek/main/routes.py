from flask import render_template
from main import main
from app import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/testing')
def test():
    return render_template('test.html')

@main.route('/about')   
def about():
    return render_template('about.html')
