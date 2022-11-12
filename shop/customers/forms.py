from wtforms import Form, SubmitField,PasswordField,StringField,TextAreaField,validators,ValidationError
from flask_wtf.file import FileField,FileRequired,FileAllowed
from flask_wtf import FlaskForm
from .models import Register

class CustomerRegisterForm(FlaskForm):
    name=StringField('Name', [validators.DataRequired(), ])
    username=StringField('Username', [validators.DataRequired(), ])
    email=StringField('Email', [validators.DataRequired(),validators.Email() ])
    password=PasswordField('Passwword', [validators.DataRequired(), validators.EqualTo('confirm', message='Both password must match')])
    confirm =PasswordField('Repeat Password', [validators.DataRequired()])
    country=StringField('Country', [validators.DataRequired(), ])
    state=StringField('State', [validators.DataRequired(), ])
    city=StringField('City', [validators.DataRequired(), ])
    contact=StringField('Contact', [validators.DataRequired(), ])
    address=StringField('Address', [validators.DataRequired(), ])
    zipcode=StringField('zip code', [validators.DataRequired(), ])
    
    profile=FileField('Profile', validators=[FileAllowed(['jpg', 'png', 'jpeg','gif'], 'Image only please')])
    submit=SubmitField('Register')
    
    
    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError('This username is already in use')
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError('This email address is already in use')
        
        
class CustomerLoginForm(FlaskForm):
     email = StringField('Email Address', [validators.DataRequired(),validators.Email()])
     password = PasswordField('Password', [validators.DataRequired(),])
    