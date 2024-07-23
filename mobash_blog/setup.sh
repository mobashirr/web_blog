#!/user/bin/bash

# set up the required lib to run flask web app

# install flask for python:
pip install flask

# create flask app.py and import flask there

# to start flask project:
# for easy access use the env var:
# export FLASK_APP=app.py
# then you can run using:
# python3 -m flask run

# to make changes without restart the app allow debug mode:
# export FLASK_ENV=development
# export FLASK_DEBUG=1


# template inhertance is good way to not repwat yourself and give flixabilty to change very easy


# pip install flask-wtf
# flask-wtf is an extension for Flask that integrates the powerful form-handling capabilities of the WTForms library.
# It simplifies the process of creating and validating web forms in Flask 


# to create random string in python
# import secrets
# secrets.token_hex(16)


# if there is problem with email validator install this:
# pip install email_validator


# the database:
# we used the sqlalckemy extention for flask
# you have to install it first:
# pip install flask-sqlalchemy

# the first database i used  in the devlopment is sqlite which is file based database
# means it stores my data base in file (binary format) and the path to that file
# is on the application configs
# use the script ./setup_db.py for intial the database and tables of the models
