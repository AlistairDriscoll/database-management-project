from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util import deprecations
deprecations.SILENCE_UBER_WARNING = True

# Executing instructions from the chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# Create a class based model with the artist table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# Create a class based model with the album table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Instead of connecting to the database directly, we will ask for a session
# Create a new instance os sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# Opens an actual session by calling the Session subclass defined above
session = Session()

# Create the database using the declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the artists table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - Select only the name column from artists
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - Select only Queen from the artist table
# artist = session.query(Artist).filter_by(Name = "Queen").first()
# print(artist.Name, artist.ArtistId, sep=" | ")

# Query 4 - Select only the artist with id of 51
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.Name, artist.ArtistId, sep=" | ")

# Query 5 - Select only the albums where artist id is 51 on the album table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - Codealong challenge to get all queen track names by composer in the track table
songs = session.query(Track).filter_by(Composer="Queen")
for track in songs:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
