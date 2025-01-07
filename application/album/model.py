from application.plugin import db
from sqlalchemy import Column, String, Date, Text
from shortuuid import uuid
from datetime import datetime


class Album(db.Model):
    __tablename__ = 'album'

    id = Column(String(64), primary_key=True, nullable=False, unique=True, default=uuid)
    create_time = Column(Date, default=datetime.now().date)
    title = Column(String(64), nullable=False, unique=True)
    summary = Column(Text, nullable=False)

    pass
