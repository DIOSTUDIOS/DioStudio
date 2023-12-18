from flask import Blueprint, render_template, request, redirect, url_for
from application.models import db, Article, Album, Category
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


articlesPage = Blueprint('articlesPage', __name__)


class ArticlesAdd(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '文章题目'})
    cSummary = StringField(label='cSummary',
                           # validators=[DataRequired(), ],
                           render_kw={'class_': 'full-width', 'placeholder': '文章简介'})
    cContent = TextAreaField(label='cContent',
                             validators=[DataRequired(), ],
                             render_kw={'class_': 'full-width', 'placeholder': '文章内容 ...'})
    cAlbum = StringField(label='cAlbum',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '文章专辑'})
    cAlbumOrder = StringField(label='cAlbumOrder',
                              validators=[DataRequired(), ],
                              render_kw={'class_': 'full-width', 'placeholder': '专辑顺序'})
    cCategory = StringField(label='cCategory',
                            # validators=[DataRequired(), ],
                            render_kw={'class_': 'full-width', 'placeholder': '文章分类'})
    cKeywords = StringField(label='cKeywords',
                            # validators=[DataRequired(), ],
                            render_kw={'class_': 'full-width', 'placeholder': '关键词组'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '新增'})

    pass


class ArticlesDelete(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '文章题目'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '删除'})

    pass


@articlesPage.route('/articles')
def articles():
    paginate = Article.query.order_by(Article.create_time.desc()).paginate(per_page=8, error_out=False)

    return render_template('page/articles.html', articles=paginate.items, paginate=paginate)


@articlesPage.route('/articles/<title>')
def get_article_by_title(title):
    article = Article.query.filter_by(title=title).first()
    content = ''.join(article.content)
    reading_quantities = article.reading_quantities + 1

    Article.query.filter_by(title=title).update({'reading_quantities': reading_quantities})

    db.session.commit()

    return render_template('page/article.html', title=title, content=content)


@articlesPage.route('/articles_by_album/<album>')
def get_articles_by_album(album):
    paginate = Article.query.filter_by(album=album).order_by(Article.create_time.desc()).paginate(per_page=8,error_out=False)

    return render_template('page/articles_by_album.html', articles=paginate.items, paginate=paginate)
    pass


@articlesPage.route('/articles_by_category/<category>')
def get_articles_by_category(category):
    paginate = Article.query.filter_by(category=category).order_by(Article.create_time.desc()).paginate(per_page=8, error_out=False)

    return render_template('page/articles_by_category.html', articles=paginate.items, paginate=paginate)
    pass


@articlesPage.route('/articles/add', methods=['GET', 'POST'])
def articles_add():
    form = ArticlesAdd()

    albums = db.session.query(Album.title).all()
    categories = db.session.query(Category.title).all()

    if request.method == 'POST':
        if form.validate_on_submit():
            article = Article(title=form.cTitle.data,
                              summary=form.cSummary.data,
                              content=form.cContent.data,
                              album=form.cAlbum.data,
                              category=form.cCategory.data,
                              keywords=form.cKeywords.data)

            db.session.add(article)
            db.session.commit()

            return redirect(url_for('articlesPage.articles'))

    return render_template('page/articles_add.html', form=form, albums=albums, categories=categories)
    pass


@articlesPage.route('/articles/delete', methods=['GET', 'POST'])
def articles_delete():
    articles_list = Article.query.all()
    form = ArticlesDelete()

    if request.method == 'POST':
        if form.validate_on_submit():
            article = Article.query.filter_by(title=form.cTitle.data).first()

            db.session.delete(article)
            db.session.commit()

        return redirect(url_for('articlesPage.articles'))

    return render_template('page/articles_delete.html', form=form, articles=articles_list)
    pass
