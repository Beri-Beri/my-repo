import csv
import sqlalchemy
import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date, ForeignKey, text
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
    try:
        with conn.begin():
            conn.execute(text("DELETE FROM clean_stations"))
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
    except Exception as e:
        print(f"Błąd podczas ładowania {csv_filename}: {e}")


def load_measures(csv_filename):
    csv_path = BASE_DIR / csv_filename
    try:
        with conn.begin():
            conn.execute(text("DELETE FROM clean_measure"))
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
    except Exception as e:
        print(f"Błąd podczas ładowania {csv_filename}: {e}")



load_stations('clean_stations.csv')
load_measures('clean_measure.csv')

conn.commit()

try:
    with conn.begin():
        result = conn.execute(text("SELECT * FROM clean_stations LIMIT 5")).fetchall()
        select_all = conn.execute(text("SELECT * FROM clean_stations")).fetchall()
        select_where = conn.execute(text("SELECT * FROM clean_stations WHERE station = 'USC00519397'")).fetchall()
        update = conn.execute(text("UPDATE clean_stations SET name = 'WAIKIKI 717.3' WHERE station = 'USC00519397'"))
        delete_where = conn.execute(text("DELETE FROM clean_stations WHERE station = 'USC00519397'"))
        delete_all = conn.execute(text("DELETE FROM clean_stations"))

        print(f"Liczba zaktualizowanych wierszy: {update.rowcount}")
        print(f"Liczba usuniętych wierszy: {delete_where.rowcount}")

    print("\nWyniki SELECT * FROM clean_stations LIMIT 5:")
    for row in result:
        print(row)

    print("\nWszystkie dane z tabeli clean_stations:")
    for row in select_all:
        print(row)

    print("\nWyniki SELECT WHERE station = 'USC00519397':")
    for row in select_where:
        print(row)
except Exception as e:
    print(f"Błąd w operacjach SQL: {e}")
conn.close()