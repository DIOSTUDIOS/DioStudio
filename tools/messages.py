from flask_mail import Mail, Message
from flask import render_template
from threading import Thread


mail = Mail()


def send_mail(subject=None, to='personalsche.sync@outlook.com', template=None, **kwargs):
    from application import app

    message = Message(subject=app.config['MAIL_SUBJECT_PREFIX'] + subject,
                      sender=app.config['MAIL_SENDER'],
                      recipients=[to])

    message.body = render_template(template + '.txt', **kwargs)
    message.html = render_template(template + '.html', **kwargs)

    thread = Thread(target=send_mail_async, args=[app, message])
    thread.start()

    return True

    pass


def send_mail_async(app, message):
    with app.app_context():
        mail.send(message)

    pass
