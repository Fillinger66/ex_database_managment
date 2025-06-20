"""
  Copyright (c) 2025 Alexandre Kavadias 

  This project is licensed under the Educational and Non-Commercial Use License.
  See the LICENSE file for details.
"""
"""
Model: Artist

This file defines the 'Artist' domain model using Python's dataclasses.
In a clean architecture, **domain models are the core business entities**
that represent the essential concepts of your application.

They are:
- Database Agnostic: An Artist object doesn't care if it came from SQLite, PostgreSQL,
  or a web API. It only represents a artist.
- Persistence Ignorant: It contains the data and behavior relevant to a 'Artist'
  in your business domain, without knowing *how* it's stored or retrieved.
- Encapsulate Domain Logic: Can include methods for validation (e.g., `is_valid_email()`)
  or business rules specific to a artist (e.g., `verify_password()`).
- Data Transfer Objects (DTOs) for the Application: They serve as structured data
  that is passed between different layers of your application (e.g., from a Repository
  to a Service, or from a Service to a presentation layer).

By defining these models, we achieve:
- Improved Type Safety: Work with `artist.name` instead of generic dictionary keys.
- Readability: Code that operates on `Artist` objects is more intuitive.
- Decoupling: Changes to the database schema or DAO implementation don't
  require changes in higher-level application logic that uses Artist objects.
"""

from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Artist:
    """
    Represents a user from Table users.
    """
    artist_id: int = field(default=None) # Use default=None for fields that might be auto-generated by DB
    name: str = field(default=None)
    
    def __init__(self, artist_id=None, name=None):
        """
        Initializes an Artist object.
        
        :param artist_id: Unique identifier for the artist, typically auto-generated by the database.
        :param name: Name of the artist.
        """
        self.artist_id = artist_id
        self.name = name

    def __post_init__(self):
        """
        Post-initialization processing for the Artist object.
        This method is automatically called after the dataclass __init__ method.
        It can be used for additional validation or transformation of the fields.
        """
        # It's useful for post-processing arguments, e.g., converting string dates from DB.
        if isinstance(self.artist_id, str):
            self.artist_id = int(self.artist_id) if self.artist_id.isdigit() else None
        
        # Domain-specific validation
        if self.name is not None and not isinstance(self.name, str):
            raise ValueError("Name must be a string.")
        


    def to_dict(self):
        """Converts the Artist object to a dictionary, useful for API responses or logging."""
        return {
            "artist_id": self.artist_id,
            "name": self.name,
        }
    
    def __str__(self):
        """String representation of the Artist object."""
        return f"Artist(artist_id={self.artist_id}, name='{self.name}')"
    
