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

        data = load_data(file_name)
        print(data[1:4])

        for i in data:
            record = CravingTip(**{
                'cz_tips':  i[0],
                'en_tips':  i[1],
                'methods':  i[2],
                # 'location': i[3],
                # 'time':     i[4],

            })
            s.add(record)  # Add all the record
        s.commit()  # Attempt to commit all the records
    except Exception as e:
        print(str(e))
        s.rollback()  # Rollback the changes on error
    finally:
        s.close()  # Close the connection
