import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.sqlite_version}")
       return conn
   except Error as e:
       print(e)
   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def add_flower_species(conn, species):
   """
   Add a new flower species into the FlowerSpecies table
   :param conn:
   :param species:
   :return: species id
   """
   sql =  '''INSERT INTO FlowerSpecies(name, family, color, blooming_season)
             VALUES(?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, species)
   conn.commit()
   return cur.lastrowid

def add_flower_details(conn, details):
    """
   Add a flower details entry into the FlowerDetails table
   :param conn:
   :param details:
   :return: details id
   """
    sql = '''INSERT INTO FlowerDetails(species_id, height_cm, fragrance, soil_type, sunlight_requirement)
             VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, details)
    conn.commit()
    return cur.lastrowid

def update(conn, table, id, **kwargs):
    """
   update attributes of a record
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )

    sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
    try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
    except sqlite3.OperationalError as e:
       print(e)

