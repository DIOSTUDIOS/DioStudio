from application.plugin import db
from application.article.model import Article, Category
from application.album.model import Album
from application.favorite.model import Favorite
from faker import Faker

import click


@click.option('--count', default=1, help='create some articles.')
def create_articles(count):
    data = Faker(locale='zh_CN')

    for i in range(count):
        article = Article()

        article.title = data.sentence()
        article.summary = data.sentence()
        article.content = data.text(max_nb_chars=6000, ext_word_list=None)
        article.album = db.session.query(Album.title).first()[0]
        article.album_order = Article.query.count() * 5
        article.category = data.sentence()
        article.keywords = data.word()
        article.sequence = Article.query.count() + 1

        db.session.add(article)

    db.session.commit()

    click.echo('随机文章 {0} 篇创建成功！'.format(count))

    pass


@click.option('--count', default=1, help='create some albums.')
def create_albums(count):
    data = Faker(locale='zh_CN')

    for i in range(count):
        album = Album()

        album.title = data.sentence()
        album.summary = data.sentence()

        db.session.add(album)

    db.session.commit()

    click.echo('随机专辑 {0} 个创建成功！'.format(count))

    pass


@click.option('--count', default=1, help='create some categories.')
def create_categories(count):
    data = Faker(locale='zh_CN')

    for i in range(count):
        category = Category()

        category.title = data.sentence()
        category.summary = data.sentence()

        db.session.add(category)

    db.session.commit()

    click.echo('随机分类 {0} 个创建成功！'.format(count))

    pass


@click.option('--count', default=1, help='create some favorite.')
def create_favorites(count):
    data = Faker(locale='zh_CN')

    for i in range(count):
        favorite = Favorite()

        favorite.title = data.sentence()
        favorite.link = data.uri()
        favorite.summary = data.sentence()

        db.session.add(favorite)

    db.session.commit()

    click.echo('随机收藏 {0} 个创建成功！'.format(count))

    pass
