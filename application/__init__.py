from flask import Flask
from application.config import Config
from application.plugin import db, migrate, mail

from application.index.views import indexPage
from application.article.views import articlePage
from application.album.views import albumPage
from application.discuss.views import discussPage
from application.favorite.views import favoritesPage
from application.about.views import aboutPage
from application.contact.views import contactPage

from application.assist.commands import create_articles, create_albums, create_categories, create_favorites


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    register_plugins(app)
    register_modules(app)
    register_assists(app)

    return app


def register_plugins(app):
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    pass


def register_modules(app):
    app.register_blueprint(indexPage)
    app.register_blueprint(articlePage)
    app.register_blueprint(albumPage)
    app.register_blueprint(discussPage)
    app.register_blueprint(favoritesPage)
    app.register_blueprint(aboutPage)
    app.register_blueprint(contactPage)
    pass


def register_assists(app):
    app.cli.command('create-articles')(create_articles)
    app.cli.command('create-albums')(create_albums)
    app.cli.command('create-categories')(create_categories)
    app.cli.command('create-favorites')(create_favorites)
    pass
