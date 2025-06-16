
import sqlite3
from db.dao.SQLiteDao import SQLiteDao

class ArtistDao(SQLiteDao):
    """
    ArtistDao is a data access object for managing artists in the database.
    It provides methods to create, read, update, and delete artist records.
    """

    tablename = "artists"
    _field_id = "ArtistId"
    _field_name = "Name"

    def __init__(self,connection: sqlite3.Connection = None,verbose: bool = False):
        """
        Initialize the DAO with a database connection.  
            :param connection: SQLite connection object. If None, ensure to set it before use.
            :param verbose: If True, print debug information. Default is False.
        """
        super().__init__(connection=connection, verbose=verbose)


    def is_table_exist(self):
        """
        Check if the artist table exists in the database.
            :return: True if the table exists, False otherwise.
        """
        return super().is_table_exist(self.tablename)
    

    def create_table_artist(self):
        """
        Create the users table in the database if it does not exist.
        This method defines the schema for the users table.
        The table includes fields for user ID, username, password hash,
        email, and creation timestamp.
        """
        self._ensure_connected()
        with self.conn:
            self.conn.execute(f"""       
                CREATE TABLE "artists"
                (
                    {self._field_id} INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    {self._field_name} NVARCHAR(120)
                )""")
            
    def get_artist_by_id(self, artist_id: int):
        """
        Retrieve an artist by their ID.
            :param artist_id: The ID of the artist to retrieve.
            :return: A dictionary representing the artist, or None if not found.
        """
        return self.execute_query(query= 
                                 f"""
                                SELECT {self._field_id}, {self._field_name}
                                FROM {self.tablename}
                                WHERE {self._field_id} = ?
                                """, 
                                params=(artist_id,), 
                                fetch_one=True, 
                                fetch_all=False)
    
    def get_artist_by_name(self, artist_name: str):
        """
        Retrieve an artist by their name.
            :param artist_name: The name of the artist to retrieve.
            :return: A dictionary representing the artist, or None if not found.
        """
        return self.execute_query(query= 
                                 f"""
                                SELECT {self._field_id}, {self._field_name}
                                FROM {self.tablename}
                                WHERE {self._field_name} = ?
                                """, 
                                params=(artist_name,), 
                                fetch_one=True, 
                                fetch_all=False)
    def get_all_artists(self):
        """
        Retrieve all artists from the database.
            :return: A list of dictionaries representing all artists.
        """
        return self.execute_query(query= 
                                 f"""
                                SELECT {self._field_id}, {self._field_name}
                                FROM {self.tablename}
                                """, 
                                fetch_one=False, 
                                fetch_all=True)
    
    def insert(self, artist_name: str):
        """
        Add a new artist to the database.
            :param artist_name: The name of the artist to add.
            :return: The ID of the newly added artist.
        """
        self._ensure_connected()
        return self._execute_insert_with_retry( 
                                query=f"""
                                    INSERT INTO {self.tablename}
                                    ({self._field_name}) 
                                    VALUES (?)
                                    """, 
                                params=(artist_name,), 
                                max_retries=5, 
                                retry_delay=0.1)
    
    def update(self, artist_id: int, artist_name: str):
        """
        Update an existing artist's name in the database.
            :param artist_id: The ID of the artist to update.
            :param new_name: The new name for the artist.
            :return: True if the update was successful, False otherwise.
        """
        self._ensure_connected()
        return self._execute_update_delete_with_retry( 
                                query=f"""
                                    UPDATE {self.tablename}
                                    SET {self._field_name} = ?
                                    WHERE {self._field_id} = ?
                                    """, 
                                params=(artist_name, artist_id), 
                                max_retries=5, 
                                retry_delay=0.1)
    
    def delete(self, artist_id: int):
        """
        Delete an artist from the database by their ID.
            :param artist_id: The ID of the artist to delete.
            :return: True if the deletion was successful, False otherwise.
        """
        self._ensure_connected()
        return self._execute_update_delete_with_retry( 
                                query=f"""
                                    DELETE FROM {self.tablename}
                                    WHERE {self._field_id} = ?
                                    """, 
                                params=(artist_id,), 
                                max_retries=5, 
                                retry_delay=0.1)