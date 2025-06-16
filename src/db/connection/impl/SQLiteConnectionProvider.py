
"""
  Copyright (c) 2025 Alexandre Kavadias 

  This project is licensed under the Educational and Non-Commercial Use License.
  See the LICENSE file for details.
"""
import os
import sqlite3
from db.connection.IDbConnectionProvider import IDbConnectionProvider # Import the new interface

class SQLiteConnectionProvider(IDbConnectionProvider): # Inherit from the interface
    """
    Concrete implementation of IDbConnectionProvider for SQLite databases.
    Provides sqlite3.Connection objects.
    """
    def __init__(self, database_path: str):
        self.database_path = database_path
        self._ensure_directories_exist()

    def _ensure_directories_exist(self):
        dir_path = os.path.dirname(self.database_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

    def get_connection(self) -> sqlite3.Connection: # Type hint specific connection for implementation
        """
        Provides a new, configured SQLite connection.
        """
        conn = sqlite3.connect(self.database_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    # No explicit close_connection here, as connections are returned and managed by caller.