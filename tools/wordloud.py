from application import app
from application.models import db, Article


def get_keywords():
    keywords = []
    result = db.session.query(Article.keywords).all()

    for item in result:
        for i in item:
            print(i.split())
            # keywords.append(i.split(' '))

    # print(keywords)
    pass


if __name__ == '__main__':
    with app.app_context():
        get_keywords()
