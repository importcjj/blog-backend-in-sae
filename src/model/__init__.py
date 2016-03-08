# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session
)


SAE_MYSQL = {
    'host': 'pohtiadtpcsy.rds.sae.sina.com.cn',
    'port': 22429,
    'username': 'chenjiaju',
    'password': '7895123jiaju',
    'database': 'blog'
}

engine = create_engine('mysql+pymysql://%s:%s@%s:%d/%s' % (
    SAE_MYSQL['username'],
    SAE_MYSQL['password'],
    SAE_MYSQL['host'],
    SAE_MYSQL['port'],
    SAE_MYSQL['database']
))

session_maker = sessionmaker(bind=engine)
Session = scoped_session(session_maker)

Base = declarative_base()

from .articles import *  # noqa
