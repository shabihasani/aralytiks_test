import psycopg2

# connection establishment
conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='Fiton',
	host='localhost',
	port='5432'
)

conn.autocommit = True

# Creating a cursor object
cursor = conn.cursor()

# query to import data from given csv
sql = '''copy demo FROM 
        'C://Users
    //Aralytiks//Desktop//pythonProject1//Sample100.csv' 
        DELIMITER ',' CSV HEADER'''

# executing above query
cursor.execute(sql)

# Display the table
cursor.execute('SELECT * FROM demo')
print(cursor.fetchall())

# Closing the connection
conn.close()
