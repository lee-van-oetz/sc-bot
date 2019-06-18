from sqlalchemy import Column,Integer, String
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()

class CravingTips(base):
	__tablename__ = 'Craving_tips'
	__table_args__ = {'sqlite_autoincrement': True}

	id = Column(Integer, primary_key = True, nullable = True)
	cz_tips = Column(String)
	en_tips = Column(String)
	methods = Column(String)
	location = Column(String)
	time = Column(String)