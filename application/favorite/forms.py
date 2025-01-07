from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddFavorite(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '网站名称'})
    cLink = StringField(label='cLink',
                        validators=[DataRequired(), ],
                        render_kw={'class_': 'full-width', 'placeholder': '网站地址'})
    cSummary = TextAreaField(label='cSummary',
                             validators=[DataRequired(), ],
                             render_kw={'class_': 'full-width','placeholder': '网站简介 ...'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '添加'})

    pass


class DelFavorite(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '网站名称'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '删除'})

    pass
