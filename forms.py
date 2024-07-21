
'''module contain all the forms of the project'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


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


class loginForm(FlaskForm):
    '''Registration form'''

    email = StringField("email", 
                        validators=[DataRequired(), Length(min=4, max=20), Email()])
    
    password = PasswordField("enter your password", 
                            validators=[DataRequired()])

    remember = BooleanField("Remember me")
    submit = SubmitField("LOG IN")