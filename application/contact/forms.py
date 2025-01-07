from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ReaderMail(FlaskForm):
    cName = StringField('cName', validators=[DataRequired(), ], render_kw={'class_': 'full-width', 'placeholder': 'Your Name'})
    cEmail = StringField('cEmail', validators=[DataRequired()], render_kw={'class_': 'full-width', 'placeholder': 'Your Email'})
    cMessage = TextAreaField('cMessage', validators=[DataRequired(), ], render_kw={'class_': 'full-width','placeholder': 'Your Message ...'})
    cSubmit = SubmitField('cSubmit', render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '发送'})

    pass
