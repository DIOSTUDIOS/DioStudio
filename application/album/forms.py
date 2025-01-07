from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddAlbum(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '专辑名称'})
    cSummary = TextAreaField(label='cSummary',
                             validators=[DataRequired(), ],
                             render_kw={'class_': 'full-width','placeholder': '专辑简介 ...'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '添加'})

    pass


class DelAlbum(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '专辑名称'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '删除'})
    pass
