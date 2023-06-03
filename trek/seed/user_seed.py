"""
This is the user_seed module.
Intended to contain all user-related functionality for the Trek project user blueprint.
Populates the database with users made from a csv file of phony user data.
"""

import os
from csv import DictReader
from app import db
from models import User, DEFAULT_IMAGE_URL

def seed_users():
    # Define a list of random first and last names to choose from
    db.drop_all()
    db.create_all()

    # Get the path to the users.csv file based on the location of this file
    users_csv = os.path.join(os.path.dirname(__file__), '..', 'generator', 'users.csv')
    with open(users_csv) as users:
        user_dicts = list(DictReader(users))
        for user_dict in user_dicts:
            email = user_dict['email']
            username = user_dict['username']
            if User.query.filter_by(email=email).first() is not None:
                print(f"Skipping user {username} with email {email}: email already exists")
            elif User.query.filter_by(username=username).first() is not None:
                print(f"Skipping user {username} with email {email}: username already exists")
            else:
                user = User(**user_dict)
                db.session.add(user)
                print(f"Added user {username} with email {email}")
        
        db.session.commit()

def seed_db():
    seed_users()

seed_db()