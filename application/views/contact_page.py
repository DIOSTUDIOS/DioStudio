from flask import Blueprint, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from tools.messages import send_mail


class ReaderMessage(FlaskForm):
    cName = StringField('cName', validators=[DataRequired(), ], render_kw={'class_': 'full-width', 'placeholder': 'Your Name'})
    cEmail = StringField('cEmail', validators=[DataRequired()], render_kw={'class_': 'full-width', 'placeholder': 'Your Email'})
    cMessage = TextAreaField('cMessage', validators=[DataRequired(), ], render_kw={'class_': 'full-width','placeholder': 'Your Message ...'})
    cSubmit = SubmitField('cSubmit', render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '发送'})

    pass


contactPage = Blueprint('contactPage', __name__)


@contactPage.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ReaderMessage()

    if request.method == 'POST':
        if form.validate_on_submit():
            cName = form.cName.data
            cEmail= form.cEmail.data
            cMessage = form.cMessage.data

            if send_mail(subject='读者来信', template='mail/contact', kwargs={'cName': cName, 'cEmail': cEmail, 'cMessage': cMessage}):
                return redirect(url_for('articlesPage.articles'))
            else:
                return redirect(url_for('contactPage.contact'))

    return render_template('page/contact.html', form=form)
