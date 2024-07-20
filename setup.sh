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


# template inhirtance is good way to not repwat yourself and give flixabilty to change very easy


# pip install flask-wtf
# this is lib comoon used in flask to create a validation pages like registeration and login pages