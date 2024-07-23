
''' my database models '''

from mobash_blog import db
from datetime import datetime


class User(db.Model):
    '''
    this table of users have the column:
    id - is from type int and primary key 
    username -  with length of 20 , unique and nullable
    email - also unique and nullable
    password - with length of 60 because its hashed
    post is a the relation for user to the Post table (just a query to join the tables togather)
    one-to-many relationship

    backref is bidirectional relationship which mean from Post you can get the user record
    with attribute author.
    '''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)    # the first arg is the name of the class not the table cause the table is lowercase

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    '''
    the post table
    id - is from type int and primary key 
    title -  with length of 100 max, nullable
    content - is a text and nullable
    date_posted - type of dataime object
    user_id - is a foreign key links the post table with the user table
    '''

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)   # this user id from author ins we passed

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
