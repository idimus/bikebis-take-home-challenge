import sqlite3
import os
import json

SQLITE_DB = f"{os.path.dirname(__file__)}/../sqlite.db"
SCHEMA_FILE = f"{os.path.dirname(__file__)}/schema.sql"
DATA_FILE = f"{os.path.dirname(__file__)}/data.json"

def generate_data():
    con = sqlite3.connect(SQLITE_DB)
    cur = con.cursor()
    
    try:
        cur.execute("SELECT * FROM bike") 
    except sqlite3.OperationalError:
        with open(SCHEMA_FILE) as f:
            sql = f.read()
            cur.executescript(sql)

    with open(DATA_FILE) as f:
        data = json.load(f)
        for bike in data["bikes"]:
            cur.execute("INSERT INTO bike VALUES (:bike_id)", bike)
        for data_point in data["data_points"]:
            cur.execute("INSERT INTO power_meter_data_point VALUES (:id, :ride_id, :bike_id, :one_min_pace, :one_min_power, :timestamp)", data_point)

    con.commit()
    con.close()


def main():
    generate_data()


if __name__ == "__main__":
    main()