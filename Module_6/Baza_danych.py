import csv
import sqlalchemy
import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date, ForeignKey

engine = create_engine('sqlite:///data.db')

metadata = MetaData()

