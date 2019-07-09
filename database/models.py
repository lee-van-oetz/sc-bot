from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()

tips_locations = Table(
    'tips_locations',
    base.metadata,
    Column('tip_id', Integer, ForeignKey('craving_tips.id')),
    Column('location_id', Integer, ForeignKey('locations.id'))
)


class CravingTip(base):
    __tablename__ = 'craving_tips'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, nullable=True)
    cz_tips = Column(String)
    en_tips = Column(String)
    methods = Column(String)

    locations = relationship('Location', secondary='tips_locations', backref='craving_tips')
    # time = Column(String)


class Location(base):
    __tablename__ = 'locations'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, nullable=True)
    name = Column(String)


