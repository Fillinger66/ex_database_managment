from typing import List, Optional
from db.dao.impl.ArtistDao import ArtistDao
from db.repositories.IRepository import IRepository
from db.models.Artist import Artist
import sqlite3

class ArtistRepository(IRepository[Artist]):
    """
    Repository for Artist entities.
    Handles conversion between domain objects and database records.
    """
    
    def __init__(self, connection: sqlite3.Connection, verbose: bool = False):
        """
        Initialize the ArtistRepository with a database connection.
            :param connection: SQLite connection object.
            :param verbose: If True, print debug information. Default is False.
        """
        self._dao = ArtistDao(connection=connection, verbose=verbose)
    
    def add(self, entity: Artist) -> Optional[Artist]:
        """Add a new artist entity to the repository.
            This method inserts a new artist into the database and sets the artist_id on the entity.
            
            :param entity: Artist entity to add.
            :return: The added Artist entity with artist_id set, or None if the operation failed.
        """
        if entity.name is None:
            return None
        
        artist_id = self._dao.insert(entity.name)
        if artist_id is None:
            return None
        # Set the artist_id on the entity after insertion
        entity.artist_id = artist_id

        return entity
    
    def get_by_id(self, entity_id: int) -> Optional[Artist]:
        """Get an artist by ID.
            This method retrieves an artist from the database by their ID.
            
            :param entity_id: The ID of the artist to retrieve.
            :return: An Artist entity if found, or None if not found.
        
        """
        db_artist = self._dao.get_artist_by_id(entity_id)
        if db_artist:
            return Artist(
                artist_id=db_artist[ArtistDao._field_id],
                name=db_artist[ArtistDao._field_name]
            )
        return None
    
    def update(self, entity: Artist) -> bool:
        """Update an existing artist.
            This method updates an artist's name in the database.
            
            :param entity: Artist entity with updated information.
            :return: True if the update was successful, False otherwise.
        """
        if entity.artist_id is None or entity.name is None:
            return False
        return self._dao.update(entity.artist_id, entity.name)
    
    def delete(self, entity_id: int) -> bool:
        """Delete an artist by ID.
            This method deletes an artist from the database by their ID.
            
            :param entity_id: The ID of the artist to delete.
            :return: True if the deletion was successful, False otherwise.
        """
        return self._dao.delete(entity_id)
    
    def get_all(self) -> List[Artist]:
        """Get all artists.
            This method retrieves all artists from the database and converts them to Artist entities.
            
            :return: A list of Artist entities.
        """
        db_artists = self._dao.get_all_artists()
        artists = []
        for db_artist in db_artists:
            artists.append(Artist(
                artist_id=db_artist[ArtistDao._field_id],
                name=db_artist[ArtistDao._field_name]
            ))
        return artists
    
    def get_by_name(self, name: str) -> Optional[Artist]:
        """Get an artist by name (additional method specific to Artist).
            This method retrieves an artist by their name.
            
            :param name: The name of the artist to retrieve.
            :return: An Artist entity if found, or None if not found.
        """
        db_artist = self._dao.get_artist_by_name(name)
        if db_artist:
            return Artist(
                artist_id=db_artist[ArtistDao._field_id],
                name=db_artist[ArtistDao._field_name]
            )
        return None