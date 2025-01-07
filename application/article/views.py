from flask import Blueprint, render_template, request, redirect, url_for
from application.plugin import db
from application.article.model import Article, Category
from application.article.forms import AddArticle, DelArticle
from application.album.model import Album


articlePage = Blueprint('articlePage', __name__)

@articlePage.route('/articles')
def get_articles():
    paginate = Article.query.order_by(Article.sequence.desc()).paginate(per_page=8, error_out=False)

    return render_template('article/get_articles.html', articles=paginate.items, paginate=paginate)


@articlePage.route('/articles/<title>')
def get_article_by_title(title):
    article = Article.query.filter_by(title=title).first()
    content = ''.join(article.content)
    reading_quantities = article.reading_quantities + 1

    Article.query.filter_by(title=title).update({'reading_quantities': reading_quantities})

    db.session.commit()

    return render_template('article/get_article_by_title.html', title=title, content=content)


@articlePage.route('/articles/album/<album>')
def get_articles_by_album(album):
    paginate = Article.query.filter_by(album=album).order_by(Article.sequence.desc()).paginate(per_page=8, error_out=False)

    return render_template('article/get_articles_by_album.html', articles=paginate.items, paginate=paginate)
    pass


@articlePage.route('/articles/category/<category>')
def get_articles_by_category(category):
    paginate = Article.query.filter_by(category=category).order_by(Article.create_time.desc()).paginate(per_page=8, error_out=False)

    return render_template('article/get_articles_by_category.html', articles=paginate.items, paginate=paginate)
    pass


@articlePage.route('/articles/add', methods=['GET', 'POST'])
def add_article():
    form = AddArticle()

    albums = db.session.query(Album.title).all()
    categories = db.session.query(Category.title).all()

    if request.method == 'POST':
        if form.validate_on_submit():
            article = Article(title=form.cTitle.data,
                              summary=form.cSummary.data,
                              content=form.cContent.data,
                              album=form.cAlbum.data,
                              album_order=form.cAlbumOrder.data,
                              category=form.cCategory.data,
                              keywords=form.cKeywords.data)

            db.session.add(article)
            db.session.commit()

        return redirect(url_for('articlePage.get_articles'))

    return render_template('article/add_article.html', form=form, albums=albums, categories=categories)


@articlePage.route('/articles/delete', methods=['GET', 'POST'])
def del_article():
    articles_list = Article.query.all()
    form = DelArticle()

    if request.method == 'POST':
        if form.validate_on_submit():
            article = Article.query.filter_by(title=form.cTitle.data).first()

            db.session.delete(article)
            db.session.commit()

        return redirect(url_for('articlePage.get_articles'))

    return render_template('article/del_article.html', form=form, articles=articles_list)
