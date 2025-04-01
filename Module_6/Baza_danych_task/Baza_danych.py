import csv
import sqlalchemy
import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date, ForeignKey
from pathlib import Path

BASE_DIR = Path(__file__).parent
engine = create_engine(f"sqlite:///{BASE_DIR / 'data.db'}")

metadata = MetaData()

clean_stations = Table(
    'clean_stations', metadata,
    Column('station', String(11), primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String(255)),
    Column('country', String(255)),
    Column('state', String(255))
)

clean_measure = Table(
    'clean_measure', metadata,
    Column('station', String(11), ForeignKey('clean_stations.station'), primary_key=True),
    Column('date', Date, primary_key=True),
    Column('precip', Float),
    Column('tobs', Float)
)

metadata.create_all(engine)

conn = engine.connect()

def load_stations(csv_filename):
    csv_path = BASE_DIR / csv_filename
    with conn.begin():
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                insert_stmt = clean_stations.insert().values(
                    station=row[0], 
                    latitude=float(row[1]),
                    longitude=float(row[2]),
                    elevation=float(row[3]),
                    name=row[4],
                    country=row[5],
                    state=row[6]
                )
                conn.execute(insert_stmt)

def load_measures(csv_filename):
    csv_path = BASE_DIR / csv_filename
    with conn.begin():
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                date_obj = datetime.datetime.strptime(row[1], "%Y-%m-%d").date()
                insert_stmt = clean_measure.insert().values(
                    station=row[0],
                    date=date_obj,
                    precip=float(row[2]) if row[2] else None,
                    tobs=float(row[3]) if row[3] else None
                )
                conn.execute(insert_stmt)

load_stations('clean_stations.csv')
load_measures('clean_measure.csv')

with conn.begin():
    result = conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall()
    select_all = conn.execute("SELECT * FROM clean_stations").fetchall()
    select_where = conn.execute("SELECT * FROM clean_stations WHERE station = 'USC00519397'").fetchall()
    update = conn.execute("UPDATE clean_stations SET name = 'WAIKIKI 717.3' WHERE station = 'USC00519397'")
    delete_where = conn.execute("DELETE FROM clean_stations WHERE station = 'USC00519397'")
    delete_all = conn.execute("DELETE FROM clean_stations")

    print(f"Liczba zaktualizowanych wierszy: {update.rowcount}")
    print(f"Liczba usuniętych wierszy: {delete_where.rowcount}")

print("Wyniki SELECT * FROM clean_stations LIMIT 5:")
for row in result:
    print(row)

print("Wszystkie dane z tabeli clean_stations:")
for row in select_all:
    print(row)

print("Wyniki SELECT WHERE station = 'USC00519397':")
for row in select_where:
    print(row)

conn.close()