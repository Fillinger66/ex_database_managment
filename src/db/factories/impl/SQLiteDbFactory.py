from db.factories.IDbFactory import IDbFactory
from db.connection.impl.SQLiteConnectionProvider import SQLiteConnectionProvider
from db.dao.impl.ArtistDao import ArtistDao
# Import other DAOs as needed

class SQLiteDbFactory(IDbFactory):
    """
    SQLiteDbFactory is a concrete implementation of IDbFactory for managing SQLite databases.
    It provides methods to create and manage database connections, initialize tables,
    and perform business logic operations related to the database.
    This factory is designed to be used in a music database application, managing entities like artists, ..."""

    def __init__(self, database_path: str, verbose: bool = False):
        """
        Initializes the SQLiteDbFactory with the database path and verbosity level.
            :param database_path: Path to the SQLite database file.
            :param verbose: If True, enables verbose logging for debugging.
        """
        super().__init__(database_path, verbose)
        self._connection_provider = SQLiteConnectionProvider(database_path)
        self.initialize_database_tables()

    def get_connection(self):
        """Provides a new SQLite connection."""
        return self._connection_provider.get_connection()

    def initialize_database_tables(self):
        """Ensures all required tables exist in the database."""
        with self.get_connection() as conn:
            # Initialize all your tables here
            artist_dao = ArtistDao(connection=conn, verbose=self.verbose)
            if not artist_dao.is_table_exist():
                artist_dao.create_table_artist()  # Fix this method name
            
            # Add other table initializations
            # album_dao = AlbumDao(connection=conn, verbose=self.verbose)
            # track_dao = TrackDao(connection=conn, verbose=self.verbose)
            # etc.

    def get_artist_dao(self):
        """Get a new instance of ArtistDao."""
        return ArtistDao(connection=self.get_connection(), verbose=self.verbose)
    

    # Business logic methods for your domain
    def create_artist(self, artist_name: str):
        """Create a new artist.
        A new connection is opened and closed for this single operation.
            :param artist_name: Name of the artist to create.
            :return: The ID of the newly created artist.
        """
        with self.get_connection() as conn:
            artist_dao = ArtistDao(connection=conn, verbose=self.verbose)
            return artist_dao.insert(artist_name)

    def get_artist_by_id(self, artist_id: int):
        """Get artist by ID.
            :param artist_id: The ID of the artist to retrieve.
            :return: A dictionary representing the artist, or None if not found.    
        """
        with self.get_connection() as conn:
            artist_dao = ArtistDao(connection=conn, verbose=self.verbose)
            return artist_dao.get_artist_by_id(artist_id)

    def get_all_artists(self):
        """Get all artists.
            :return: A list of dictionaries representing all artists in the database.
        """
        with self.get_connection() as conn:
            artist_dao = ArtistDao(connection=conn, verbose=self.verbose)
            return artist_dao.get_all_artists()
    
    def get_artist_by_name(self, artist_name: str):
        """Get an artist by name.
            :param artist_name: The name of the artist to retrieve.
            :return: A dictionary representing the artist, or None if not found.
        """
        with self.get_connection() as conn:
            artist_dao = ArtistDao(connection=conn, verbose=self.verbose)
            return artist_dao.get_artist_by_name(artist_name)
        
    def delete_artist(self, artist_id: int):
        """Delete an artist by ID.
            :param artist_id: The ID of the artist to delete.
            :return: True if the artist was successfully deleted, False otherwise.
        """
        with self.get_connection() as conn:
            artist_dao = ArtistDao(connection=conn, verbose=self.verbose)
            return artist_dao.delete(artist_id)
        
    def update_artist(self, artist_id: int, artist_name: str):
        """Update an artist's name.
            :param artist_id: The ID of the artist to update.
            :param new_name: The new name for the artist.
            :return: True if the artist was successfully updated, False otherwise.
        """
        with self.get_connection() as conn:
            artist_dao = ArtistDao(connection=conn, verbose=self.verbose)
            return artist_dao.update(artist_id, artist_name)
    

    # Add similar methods for other entities (albums, tracks, etc.)