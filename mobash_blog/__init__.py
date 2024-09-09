
'''the module mobash_blog'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b54af37ce9b4df9c42b12577ad7fd3fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
encrypter = Bcrypt(app)


# we put it at the last because we don't need circular import again (routes need the app var)
from mobash_blog import routes