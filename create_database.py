import sqlite3

connection = sqlite3.connect('coin_database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS coins (coin_id integer PRIMARY KEY, \
    description text, value real, conservation_state text, country text, year integer)"

create_coin = "INSERT INTO coins VALUES (0, 'Moeda de um real', 1, 'BC', 'Brazil', 2023)"

cursor.execute(create_table)
cursor.execute(create_coin)

connection.commit()
connection.close()
