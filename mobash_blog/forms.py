
'''module contain all the forms of the project'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mobash_blog.models import User
from mobash_blog import encrypter
from flask import render_template, url_for,flash,redirect


class RegistrationForm(FlaskForm):
    '''Registration form'''

    username = StringField("username", 
                        validators=[DataRequired(), Length(min=4, max=20)])

    email = StringField("email", 
                        validators=[DataRequired(), Length(min=4, max=20), Email()])
    
    password = PasswordField("enter your password", 
                            validators=[DataRequired()])
    
    confirm_password = PasswordField("confirm your password",
                            validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign up")

    def validate_username(self, username):
        ''' validate that the username is unique'''
        print(username)
        user_exist = User.query.filter_by(username=username).first()
        if user_exist:
            raise ValidationError("this username is already taken try another one.")

    def validate_email(self, email):
        ''' validate that the email is unique'''
        user_exist = User.query.filter_by(email=email).first()
        if user_exist:
            raise ValidationError("this email is already used try another one.")

class loginForm(FlaskForm):
    '''Registration form'''

    email = StringField("email", 
                        validators=[DataRequired(), Length(min=4, max=20), Email()])
    
    password = PasswordField("enter your password", 
                            validators=[DataRequired()])

    remember = BooleanField("Remember me")
    submit = SubmitField("LOG IN")

    def validate_correct_info(self):
        ''' check if the password is correct'''
        user_exist = User.query.filter_by(email=self.email.data).first()
        if user_exist and encrypter.check_password_hash(user_exist.password, self.password.data):
            return True
        else:
            flash(f"your email or password isn't correct", 'danger')
            return redirect(url_for('login'))
