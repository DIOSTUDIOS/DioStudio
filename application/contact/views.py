from flask import Blueprint, render_template, redirect, url_for, request, flash
from application.contact.forms import ReaderMail
from application.assist.sendmail import send_mail

contactPage = Blueprint('contactPage', __name__)


@contactPage.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ReaderMail()

    if request.method == 'POST':
        if form.validate_on_submit():
            cName = form.cName.data
            cEmail= form.cEmail.data
            cMessage = form.cMessage.data

            if send_mail(subject='读者来信', template='mail/contact', kwargs={'cName': cName, 'cEmail': cEmail, 'cMessage': cMessage}):
                flash(message='邮件发送成功！')
                return redirect(url_for('articlePage.get_articles'))
            else:
                flash(message='邮件发送失败！')
                return redirect(url_for('contactPage.contact'))

    return render_template('contact/contact.html', form=form)
