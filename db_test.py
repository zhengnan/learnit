#!/usr/bin/env python
# -*- coding: utf-8 -*-

'This is a test of ORM by using SQLAlchemy'

__author__ = 'focus'
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(String(20), primary_key=True)
	name = Column(String(20))

def test():
	engine = create_engine('mysql+mysqlconnector://root:passwd@localhost:3306/test')
	DBSession = sessionmaker(bind=engine)

	session = DBSession()
	#user = User()

	#user = session.query(User).filter(User.id=='2').one()
	user = session.query(User).all()

	print user[0].name

	session.close()

if __name__ == '__main__':
	test()
