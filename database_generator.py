import csv

from database import Session
from database.models import *


def load_data(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


Base = declarative_base()

if __name__ == "__main__":
    s = Session()

    try:
        file_name = "database/craving_tips.csv"
        print("\n1\n")
        data = load_data(file_name)
        print(data)
        
        k=0
        for i in data:
            if k==0:
                k+=1
                continue
            locations = ["home","work","social gathering","leisure","other"]

            locations_applicable = []
            
            for j in range(0,4):

                temp = int(i[3][j])
                if(temp != 0):
                    locations_applicable.append(locations[temp])
            
            print(locations_applicable)
            #Record for table "craving_tips"; A Craving_Tip object
            record1 = CravingTip(**{
                'cz_tips':  i[0],
                'en_tips':  i[1],
                'methods':  i[2],
                # 'location': i[3],
                # 'time':     i[4],

            })

            #Record for table "locations"; A "Location" Class object
            # TODO: fetch applicable locations
            locs = s.query(Location).filter(Location.name.in_(locations_applicable)).all()
            print(locs.name)
            # TODO: relate fetched locations to inserted tip record
            record1.locations.extend(locs)
          

        s.commit()  # Attempt to commit all the records
    except Exception as e:
        print("\nblabla\n",str(e))
        s.rollback()  # Rollback the changes on error
    finally:
        s.close()  # Close the connection
