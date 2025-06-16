"""
  Copyright (c) 2025 Alexandre Kavadias 

  This project is licensed under the Educational and Non-Commercial Use License.
  See the LICENSE file for details.
"""
from abc import ABC, abstractmethod
from typing import Any # For generic connection type

class IDbFactory(ABC):
    """
    Abstract base class for database initialization and connection provisioning.
    Defines common methods for setting up a database environment.
    """

    def __init__(self, database_path: str, verbose: bool = False):
        self.database_path = database_path
        self.verbose = verbose

    @abstractmethod
    def get_connection(self) -> Any:
        """
        Abstract method to provide a database connection.
        Concrete implementations will return a connection object specific to their database.
        """
        pass

    @abstractmethod
    def initialize_database_tables(self) -> None:
        """
        Abstract method to ensure all necessary database tables are created.
        This method should be safely callable multiple times.
        """
        pass