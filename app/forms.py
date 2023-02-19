from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired()])
    msg = StringField('Message', widget=TextArea(), validators=[InputRequired()])
    submit = SubmitField('Send', validators=[InputRequired()])
