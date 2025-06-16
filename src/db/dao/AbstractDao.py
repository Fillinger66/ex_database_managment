"""
  Copyright (c) 2025 Alexandre Kavadias 

  This project is licensed under the Educational and Non-Commercial Use License.
  See the LICENSE file for details.
"""
from abc import ABC, abstractmethod
import threading
from typing import Any, List, Tuple, Union, Optional, Dict

class AbstractDao(ABC):
    """
    Abstract base class for core Data Access Object functionalities.
    Defines generic database interaction primitives that all concrete
    database-specific DAOs must implement.
    """
    def __init__(self, connection: Any = None, verbose: bool = False):
        """
        Initialize the DAO with a database connection.
        The 'connection' type is generic (Any) because it varies by database driver.
        """
        self.conn = connection
        self.verbose = verbose
        # This lock is generic for Python-level synchronization, useful if connection
        # objects are shared across threads, regardless of the specific database.
        self._write_lock = threading.Lock()

    @abstractmethod
    def _ensure_connected(self):
        """
        Abstract method to ensure that a database connection object has been set
        and is in a usable state. Implementation will be database-specific.
        """
        pass

    @abstractmethod
    def is_table_exist(self, table_name: str) -> bool:
        """
        Abstract method to check if a specific table exists in the database.
        Implementation will vary based on the database's system tables (e.g., sqlite_master, information_schema).
        """
        pass

    @abstractmethod
    def execute_query(self, query: str, params: Optional[Tuple] = None, fetch_one: bool = False, fetch_all: bool = False) -> Union[Any, List[Any], None]:
        """
        Abstract method to execute a read query on the database.
        Does NOT commit changes. Returns raw database-specific results (e.g., rows from driver).
        The return type 'Any' is used as the exact row/result type varies by database driver.
        """
        pass
    
    @abstractmethod
    def _execute_with_retry(self, query: str, params: Optional[Tuple] = None, max_retries: int = 5, retry_delay: float = 0.1) -> bool:
        """
        Abstract helper method to execute a write query (INSERT, UPDATE, DELETE)
        with retry logic for database-specific locking/concurrency issues.
        Handles commit/rollback for the specific operation.
        """
        pass