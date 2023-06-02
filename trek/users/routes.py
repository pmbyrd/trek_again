from flask import redirect, render_template, flash
from sqlalchemy.exc import IntegrityError
from users import users

@users.route('/')
def index():
    return render_template('index.html')