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
