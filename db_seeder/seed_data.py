import os
import random
import string
import datetime
import json

"""
Generate seed data for the sqlite database.
We know that the algorithm might not generate realistic data (e.g. unrealistic jump in pace/power).
However, for the use case of this project, we don't need realistic data.
"""

def rand_timestamp(date: datetime.date):
    start_timestamp = int(datetime.datetime(date.year, date.month, date.day, 0, 0, 0).strftime("%s"))
    end_timestamp = int(datetime.datetime(date.year, date.month, date.day, 23, 59, 59).strftime("%s"))
    return random.randint(start_timestamp, end_timestamp)

def gen_id(length: int=8):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str

def generate_ride(bike_id: str, duration: int, start_time: int) -> list:

    ride_id = gen_id()
    data_points = []
    for i in range(duration):
        data_point = {
            "id": gen_id(),
            "ride_id": ride_id,
            "bike_id": bike_id,
            "one_min_pace": random.uniform(5, 40),
            "one_min_power": random.uniform(80, 200),
            "timestamp": start_time + i*60
        }
        data_points.append(data_point)

    return data_points


def main():
    bikes = [{"bike_id": gen_id()} for _ in range(4)]
    with (open(f"{os.path.dirname(__file__)}/data.json", "w")) as f:
        data_points = []
        for bike in bikes:
            ride_date_day = ride_date_month = 1
            for _ in range(random.randint(1, 100)):
                if ride_date_day > 27:
                    ride_date_day = 1
                    ride_date_month += 1
                else:
                    ride_date_day += 1
                
                ride_date = datetime.date(2023, ride_date_month, ride_date_day)
                ride_start_time = rand_timestamp(ride_date)
                ride_duration = random.randint(1, 120)
                ride_data = generate_ride(bike["bike_id"], ride_duration, ride_start_time)
                data_points.extend(ride_data)

        f.write(json.dumps({
            "bikes": bikes,
            "data_points": data_points
        }))

if __name__ == "__main__":
    main()