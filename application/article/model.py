from application import db
from sqlalchemy import Column, String, Date, Text, Integer, Boolean
from shortuuid import uuid
from datetime import datetime


class Article(db.Model):
    __tablename__ = 'article'

    id = Column(String(64), primary_key=True, nullable=False, unique=True, default=uuid)
    author = Column(String(64), default='diostudio')
    create_time = Column(Date, default=datetime.now().date)
    title = Column(String(64), nullable=False, unique=True, index=True)
    summary = Column(String(128))
    content = Column(Text, nullable=False)
    album = Column(String(64), default=None)
    album_order = Column(String(64))
    category = Column(String(64), default=None)
    keywords = Column(String(128), default=None)
    reading_quantities = Column(Integer, default=0)
    comment_quantities = Column(Integer, default=0)
    is_show = Column(Boolean, default=True)
    is_top = Column(Boolean, default=False)
    sequence = Column(Integer, autoincrement=True)

    pass


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(String(64), primary_key=True, nullable=False, unique=True, default=uuid)
    title = Column(String(64), nullable=False)
    summary = Column(Text, nullable=False)

    pass
