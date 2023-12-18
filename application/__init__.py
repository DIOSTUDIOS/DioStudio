from flask import Flask
from application.views.home_page import homePage
from application.views.album_page import albumPage
from application.views.articles_page import articlesPage
from application.views.favorites_page import favoritesPage
from application.views.discuss_page import discussPage
from application.views.about_page import aboutPage
from application.views.contact_page import contactPage
from application.views.errors_page import pageNotFound
from application.models import db
from flask_migrate import Migrate
from tools.commands import create_articles, create_favorites, create_albums, create_categories
from tools.messages import mail

import os

app = Flask(__name__, template_folder='templates', static_folder='static')
# 数据库相关设置
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# WTForms 相关设置
app.config['SECRET_KEY'] = 'wE1lpO$ivbY4luRO'
# Mail 相关设置
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'diostudio@foxmail.com'
app.config['MAIL_PASSWORD'] = 'lasgikitgydubjaa'
app.config['MAIL_DEFAULT_SENDER'] = ('DIOSTUDIO', 'diostudio@foxmail.com')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_SUBJECT_PREFIX'] = '[DIOSTUDIO]'
app.config['MAIL_SENDER'] = 'DIOSTUDIO <diostudio@foxmail.com>'
# 蓝图
app.register_blueprint(homePage)
app.register_blueprint(albumPage)
app.register_blueprint(articlesPage)
app.register_blueprint(favoritesPage)
app.register_blueprint(discussPage)
app.register_blueprint(aboutPage)
app.register_blueprint(contactPage)
app.register_blueprint(pageNotFound)
# 自定义命令
app.cli.command('create-articles')(create_articles)
app.cli.command('create-favorites')(create_favorites)
app.cli.command('create-albums')(create_albums)
app.cli.command('create-categories')(create_categories)


db.init_app(app)
migrate = Migrate(app, db)

mail.init_app(app)
