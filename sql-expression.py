from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)
from sqlalchemy.util import deprecations
deprecations.SILENCE_UBER_WARNING = True

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", Integer),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "name" column from the artists directory
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only "Queen" from the artists table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only the artist with the id of 51
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with the artistid of 51
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - codealong challenge
    select_query = track_table.select().where(track_table.c.Composer == "Queen")



    results = connection.execute(select_query)
    for result in results:
        print(result)
