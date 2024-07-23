
'''the module mobash_blog'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b54af37ce9b4df9c42b12577ad7fd3fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
db = SQLAlchemy(app)

from mobash_blog import routes  # we put at the last because we don't need circular import again