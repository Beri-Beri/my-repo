import csv
import sqlalchemy
import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date, ForeignKey

engine = create_engine('sqlite:///data.db')

metadata = MetaData()

clean_stations = Table(
    'clean_stations', metadata,
    Column('station', String(11), primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String(255) ),
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

def load_stations(csv_file):
    with conn.begin():
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
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

def load_measures(csv_file):
    with conn.begin():
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
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