from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, IntegerField 
from wtforms.validators import InputRequired 
from flask_wtf.file import FileField, FileAllowed, FileRequired, DataRequired
 
 
 
class SignUpForm(FlaskForm): 
     first_name = StringField('First Name', validators=[InputRequired()]) 
     last_name = StringField('Last Name', validators=[InputRequired()]) 
     age = IntegerField('Age', validators=[InputRequired()]) 
     gender = SelectField(label='Gender', choices=[("Male", "Male"), ("Female", "Female")]) 
     biography = StringField('Biography', validators=[InputRequired()]) 
     photo=FileField('Image', validators=[FileRequired()])