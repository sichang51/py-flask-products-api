import sqlite3

def connect_to_db():
  conn = sqlite3.connect("database.db")
  conn.row_factory = sqlite3.Row
  return conn

def initial_setup():
  conn = connect_to_db()
  conn.execute(
    """
    DROP TABLE IF EXISTS products;
    """
  )
  conn.execute(
    """
    CREATE TABLE products (
    id INTEGER PRIMARY KEY NOT NULL,
    image_url TEXT,
    title TEXT,
    rating TEXT,
    description TEXT,
    cast TEXT,
    genre TEXT
    )
    """
  )
  conn.commit()
  print("Table created successfully")

  products_seed_data = [
    ("https://upload.wikimedia.org/wikipedia/en/e/ef/Taken_trilogy_DVD_cover.jpg", "Taken", "PG-13", "When his daughter is kidnapped by a gang of human traffickers while vacationing inf Paris, a former spy must pull out all the stops to save her", "Liam Neeson, Maggie Grace, Famke Janssen", "Action"),
    ("https://www.commonsensemedia.org/sites/default/files/styles/ratio_2_3_medium/public/product-images/csm-movie/boyz-min.jpg", "Boyz N the Hood", "R", "A high school student living with his stern, loving father in South Central Los Angeles get drawn into the neighborhood's gangs, drugs and violence", "Ice Cube, Cuba Gooding Jr., Laurence Fishburne", "Drama"),
    ("https://cps-static.rovicorp.com/2/Open/Paramount_Pictures_1103/Program/4225430/_derived_jpg_q90_310x470_m0/AnchormanLegendOfRonBurgundy-2-3.jpg", "Anchorman", "PG-13", "In 1970s San Diego, a hotshot anchor and his news team work hard and party harder until an ambitious new reporter shakes up the station with her talent", "Will Farrell, Christina Applegate, Paul Rudd", "Comedy"),
  ]
  conn.executemany(
    """
    INSERT INTO products (image_url, title, rating, description, cast, genre)
    VALUES (?,?,?,?,?,?)
    """,
    products_seed_data,
  )
  conn.commit()
  print("Seed data created successfully")

  conn.close()


if __name__ == "__main__":
    initial_setup()

def products_all():
   conn = connect_to_db()
   rows = conn.execute(
      """
      SELECT * FROM products
      """
   ).fetchall()
   return [dict(row) for row in rows]