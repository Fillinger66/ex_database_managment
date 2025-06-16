from db.factories.IDbFactory import IDbFactory
from db.connection.impl.SQLiteConnectionProvider import SQLiteConnectionProvider
from db.repositories.impl.ArtistRepository import ArtistRepository
from db.dao.impl.ArtistDao import ArtistDao
from typing import Optional
from db.models.Artist import Artist

# Import other repositories as needed

class SQLiteRepositoryFactory(IDbFactory):


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
                artist_dao.create_table_artist()
            
            # Add other table initializations
            # album_dao = AlbumDao(connection=conn, verbose=self.verbose)
            # etc.

    def get_artist_repository(self) -> ArtistRepository:
        """Get an ArtistRepository with a new connection."""
        return ArtistRepository(connection=self.get_connection(), verbose=self.verbose)
    
   
