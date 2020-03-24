from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 

class inputForm(FlaskForm):
	input = StringField('Input')
	submit = SubmitField('Submit')