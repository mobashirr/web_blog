#!/user/bin/bash

# set up the required lib to run flask web app

# first of all i am using python virual enviroment (env dir)

# you may need to install the venv if you want to create another venv 
# but its not required to run the project:
# sudo apt install python3.10-venv
# if you installed it and have any probelm with permisson use:
# sudo chown -R $USER:$USER myenv


# so you can use it with out dealing with all configs and dependency by your own
# to create venv:  python3 -m venv myenv
# to access the venv source myenv/bin/activate
# to list the packeges : pip list
# to exit the venv: deactivate
# to create requirments file: pip freeze > requirements.txt
# to install depencency from the requirment file: pip install -r requirements.txt


# access the venv
source env/bin/activate

# install flask for python:
#   pip install flask


# create flask app.py and import flask there
# to start flask project:
# for easy access use the env var:
# export FLASK_APP=app.py
# then you can run using:
#  python3 -m flask run

# to make changes without restart the app allow debug mode:
# export FLASK_ENV=development
# export FLASK_DEBUG=1


# template inhertance is good way to not repwat yourself and give flixabilty to change very easy


## pip install flask-wtf
# flask-wtf is an extension for Flask that integrates the powerful form-handling capabilities of the WTForms library.
# It simplifies the process of creating and validating web forms in Flask 


# to create random string in python
# import secrets
# secrets.token_hex(16)


# if there is problem with email validator install this:
## pip install email_validator


# the database:
# we used the sqlalckemy extention for flask
# you have to install it first:
## pip install flask-sqlalchemy

# the first database i used  in the devlopment is sqlite which is file based database
# means it stores my data base in file (binary format) and the path to that file
# is on the application configs
## use the script ./setup_db.py for intial the database and tables of the models
./mobash_blog/setup_db.py


# for me to be able to hash the password in my database (for security and privacy reasons)
# i can use any hashing algorithm like the one flask bcrypt extention provide
## pip install flask-bcrypt

# notes in encryption
# bcrypt.generate_password_hash(password).decode('utf-8')
# the hash algorithm do something called SALTING
# which means that even of you pass the same value it generate diffrent hash value
# so when you need to compare the input of the user and the pass in the db use this func:
# bcrypt.check_password_hash(hashed_password, password) # return boolean
# what it does is to remove the salt part and compare the hashes

