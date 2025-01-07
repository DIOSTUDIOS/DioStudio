from application.plugin import db
from sqlalchemy import Column, String
from shortuuid import uuid


class Favorite(db.Model):
    __tablename__ = 'favorite'

    id = Column(String(64), primary_key=True, nullable=False, unique=True, default=uuid)
    title = Column(String(64), nullable=False, unique=True)
    link = Column(String(256), nullable=False)
    summary = Column(String(256))

    pass
