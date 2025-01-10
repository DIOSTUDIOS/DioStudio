from flask import Blueprint, render_template
from application.article.model import Article


indexPage = Blueprint('indexPage', __name__)


@indexPage.route('/')
def index():
    article = Article.query.order_by(Article.sequence.desc()).first()
    content = ''.join(article.content)

    return render_template('index/index.html', content=content)
