from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_engine = create_engine('sqlite:///database/db.sqlite3')
Session = sessionmaker(bind=db_engine)
