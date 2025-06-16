from abc import ABC, abstractmethod
import os

from typing import Any

class IDbConnectionProvider(ABC):
    """
    Abstract Base Class (Interface) for Database Connection Providers.
    Defines the contract for any class that provides database connections.

    Higher-level components (like factories or repositories) will depend
    on this interface, enabling easy swapping of database technologies
    without modifying the consuming code.
    """

    @abstractmethod
    def get_connection(self) -> Any:
        """
        Provides a database connection.
        Could be sqlite3.Connection, mysql.connector.Connection, etc.

        The specific type of connection returned depends on the concrete implementation.
        It is the responsibility of the caller to manage (e.g., close) this connection
        unless the implementation handles connection pooling/management internally.
        """
        pass