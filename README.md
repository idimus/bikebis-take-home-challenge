# bikebi-take-home-challenge

## db_seeder

_Note:_ For the take-home challenge you do not need to touch this python package. The following paragraph is just added
for documentation purposes. Executing the seeding script again will fail because of a unique constraint on the bike primary key (sqlite3.IntegrityError: UNIQUE constraint failed: bike.bike_id).

Make sure you have at least python 3.9 installed.

To help you encapsulate the required python packages create a [virtual environment](https://docs.python.org/3/library/venv.html).

After activating it, update pip and install the required packages by running `pip install --upgrade pip && pip install -r requirements.txt`.

To seed the database run `python main.py`
