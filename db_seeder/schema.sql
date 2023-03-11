CREATE TABLE IF NOT EXISTS "bike" (
    bike_id text PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS "power_meter_data_point" (
    id text PRIMARY KEY,
    bike_id text NOT NULL,
    ride_id text NOT NULL,
    timestamp text NOT NULL,
    one_min_power float NOT NULL,
    one_min_pace float NOT NULL,
    FOREIGN KEY (bike_id) REFERENCES bike (bike_id)
        ON DELETE CASCADE 
        ON UPDATE NO ACTION
);