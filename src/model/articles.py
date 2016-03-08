# -*- coding: utf-8 -*-
from src.model import (
    Base,
    Session
)
from sqlalchemy import (
    Column,
    Integer,
    SmallInteger,
    String,
    Text,
    DateTime,
    func
)


class Article(Base):

    __tablename__ = 'tb_article'
    __writeable__ = ['title', 'author', 'markdown', 'is_delete']

    id = Column(Integer, primary_key=True)
    title = Column(String(255), default='')
    author = Column(String(50), default='')
    markdown = Column(Text, default='')
    is_delete = Column(SmallInteger, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        Session.add(obj)
        Session.flush(obj)
        return obj

    def update(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__writeable__ and v is not None:
                setattr(self, k, v)
        Session.add(self)
        Session.flush()

    def remove(self):
        self.is_delete = 1
        Session.add(self)

    @classmethod
    def get(cls, id):
        return Session.query(cls).\
            filter(cls.id == id).first()

    @classmethod
    def mget(cls, ids, status=0, offset=0, limit=12):
        if not ids:
            return []
        query = Session.query(cls).\
            filter(cls.id.in_(ids))
        if status is not None:
            query = query.filter(cls.is_delete == status)
        return query.offset(offset).limit(limit).all()


class Label(Base):

    __tablename__ = 'tb_label'
    __writeable__ = ['name', 'color', 'is_delete']

    id = Column(Integer, primary_key=True)
    name = Column(String(50), default='')
    color = Column(String(50), default='#FFF')
    is_delete = Column(SmallInteger, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        Session.add(obj)
        Session.flush()
        return obj

    def update(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__writeable__ and v is not None:
                setattr(self, k, v)
        Session.add(self)
        Session.flush()

    def remove(self):
        self.is_delete = 1
        Session.add(self)

    @classmethod
    def mget(cls, ids, status=0, offset=0, limit=10):
        query = Session.query(cls).\
            filter(cls.id.in_(ids))
        if status is not None:
            query = query.filter(cls.is_delete == status)
        return query.offset(offset).limit(limit).all()


class ArticleLabel(Base):

    __tablename__ = 'tb_article_label'
    __writeable__ = []

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, default=0)
    label_id = Column(Integer, default=0)
    is_delete = Column(SmallInteger, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        Session.add(obj)
        Session.flush()
        return obj

    def remove(self):
        self.is_delete = 1
        Session.add(self)

    @classmethod
    def article_ids(cls, label_ids, status=0, offset=0, limit=10):
        if not label_ids:
            return []
        query = Session.query(cls).\
            filter(cls.label_id.in_(label_ids))
        if status is not None:
            query = query.filter(cls.is_delete == status)
        return [art.id for art in query.offset(offset).limit(limit)]

    @classmethod
    def label_ids(cls, article_id):
        query = Session.query(cls).\
            filter(cls.article_id == article_id).\
            filter(cls.is_delete == 0)
        return [label.id for label in query]
