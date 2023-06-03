from app import db
from flask_login import UserMixin
from datetime import datetime

DEFAULT_IMAGE_URL = "https://loading.io/icon/tpi8gu"


class User(UserMixin, db.Model):
    """Creates a user model for the database.
    
    Attributes:
        id: An integer representing the user's id.
        username: A string representing the user's username.
        first_name: A string representing the user's first name.
        last_name: A string representing the user's last name.
        email: A string representing the user's email.
        avatar: A string representing the user's avatar.
        password: A string representing the user's password.
        bio: A string representing the user's bio.
        location: A string representing the user's location.
        
    """

    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.Text, nullable=False, unique=True)
    
    first_name= db.Column(db.Text, nullable=False)
    
    last_name = db.Column(db.Text, nullable=False)
    
    email = db.Column(db.Text, nullable=False, unique=True)
    
    avatar = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
    password = db.Column(db.Text, nullable=False)
    
    bio = db.Column(db.Text, nullable=True)
    
    location = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # TODO: Add a relationship to the posts table and other tables as needed.
    
    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
    

    @property
    def full_name(self):
        """Returns the user's full name"""
        
        return f"{self.first_name} {self.last_name}"