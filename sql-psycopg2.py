import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object to the database
cursor = connection.cursor()

# Query 1 - select all records from the artist table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - selects only the name column from the artist table
# cursor.execute('SELECT "Name" from "Artist"')

# Query 3 - selects only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - selects queen by their idnumber instead of name
# cursor.execute('SELECT * FROM "Artist WHERE "ArtistId" = %s', [51])

# Query 5 - selects only the albums with artistId number of 51 from the albums table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - selects all tracks from the Track table where the composer is called Queen
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - challenge from walkthrough to find info of my own from artist names I've seen while testing
# cursor.execute('SELECT * from "Track" WHERE "Composer" = %s', ["Johann Sebastian Bach"])

# Query 8 - challenge from walkthrough to see what happens when no results are there
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Test"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)