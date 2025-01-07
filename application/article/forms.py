from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddArticle(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '文章题目'})
    cSummary = StringField(label='cSummary',
                           validators=[DataRequired(), ],
                           render_kw={'class_': 'full-width', 'placeholder': '文章简介'})
    cContent = TextAreaField(label='cContent',
                             validators=[DataRequired(), ],
                             render_kw={'class_': 'full-width', 'placeholder': '文章内容 ...'})
    cAlbum = StringField(label='cAlbum',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '文章专辑'})
    cAlbumOrder = StringField(label='cAlbumOrder',
                              # validators=[DataRequired(), ],
                              render_kw={'class_': 'full-width', 'placeholder': '专辑顺序'})
    cCategory = StringField(label='cCategory',
                            validators=[DataRequired(), ],
                            render_kw={'class_': 'full-width', 'placeholder': '文章分类'})
    cKeywords = StringField(label='cKeywords',
                            # validators=[DataRequired(), ],
                            render_kw={'class_': 'full-width', 'placeholder': '关键词组'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn btn--primary btn-wide btn--large full-width', 'value': '上传文章'})

    pass


class DelArticle(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '文章题目'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '删除'})

    pass
