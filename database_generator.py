import csv
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def Load_Data(file_name):
    with open(file_name, 'r') as f:

        reader = csv.reader(f)
        data = list(reader)
    return data

Base = declarative_base()

class Craving_tips(Base):
    
    __tablename__ = 'Craving_tips'
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = Column(Integer, primary_key=True, nullable=False) 
    cz_tips = Column(String)
    en_tips = Column(String)
    methods = Column(String)
    location = Column(String)
    time = Column(String)
    
if __name__ == "__main__":

    engine = create_engine('sqlite:///Craving_tips.db')
    Base.metadata.create_all(engine)

    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "Craving tips.csv"
      
        data = Load_Data(file_name) 
        print(data[1:4])

        for i in data:
            record = Craving_tips(**{
                'cz_tips' : i[0],
                'en_tips' : i[1],
                'methods' : i[2],
                'location' : i[3],
                'time' : i[4],
                
            })
            print("1")
            s.add(record) #Add all the record
        s.commit() #Attempt to commit all the records
    except Exception as e:
        print(str(e))
        s.rollback() #Rollback the changes on error
    finally:
        s.close() #Close the connection