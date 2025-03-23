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

def delete_all(conn, table):
     """
   Delete all rows from table
   :param conn: Connection to the SQLite database
   :param table: table name
   :return:
   """
     sql = f'DELETE FROM {table}'
     cur = conn.cursor()
     cur.execute(sql)
     conn.commit()

     print('Deleted')

def delete_where(conn, table, **kwargs):
    """
   Delete from table where attributes from
   :param conn:  Connection to the SQLite database
   :param table: table name
   :param kwargs: dict of attributes and values
   :return:
   """
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v, )
    q = " AND ".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print("Deleted")

if __name__ == '__main__':
    
    create_flower_species_sql = """
    CREATE TABLE IF NOT EXISTS FlowerSpecies(
    id INTEGER PRIMARY KEY,
    name text NOT NULL,
    family text NOT NULL,
    color text NOT NULL,
    blooming_season text NOT NULL
    );
    """

    create_flower_details_sql = """
    CREATE TABLE IF NOT EXISTS FlowerDetails (
    id INTEGER PRIMARY KEY,
    species_id INTEGER NOT NULL,
    height_cm INTEGER NOT NULL,
    fragrance BOOLEAN NOT NULL,
    soil_type text NOT NULL,
    sunlight_requirement text NOT NULL,
    FOREIGN KEY (species_id) REFERENCES FlowerSpecies (id)
    );
    """

    db_file = "database.db"

    conn = create_connection(db_file)
    execute_sql(conn, create_flower_species_sql)
    execute_sql(conn, create_flower_details_sql)

    species = ("Rose", "Rosaceae", "Red", "Spring")
   
    species_id = add_flower_species(conn, species)

    details = (
        species_id,
        50,
        True,
        "Loamy",
        "Full Sun"
    )
    
    details_id = add_flower_details(conn, details)

    print(species_id, details_id)
    conn.commit()

    update(conn, "FlowerDetails", 2, soil_type="Sandy")

    delete_where(conn, "FlowerDetails", id=3)
    delete_all(conn, "FlowerDetails")

    if conn is not None:
        conn.close()
        