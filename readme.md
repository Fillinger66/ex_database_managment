# Music Database Management System

A Python-based database management system demonstrating clean architecture principles with SQLite integration. This project implements a layered architecture with Data Access Objects (DAO), Repository patterns, and Factory patterns for managing music-related entities.

## 🎯 Project Overview

This project showcases a well-structured database management system built with Python, following clean architecture principles and SOLID design patterns. It provides multiple abstraction layers for database operations, making it easy to extend and maintain.

**This project can give you the basis to interact with a database. For sure it can still be improve and I invite you to try it**

## 📁 Project Structure

```
ex_database_managment/
├── readme.md
├── database/
│   └── music.db                    # SQLite database file
└── src/
    ├── __init__.py
    ├── main.py                     # Main application entry point
    └── db/
        ├── __init__.py
        ├── connection/             # Database connection management
        │   ├── __init__.py
        │   ├── IDbConnectionProvider.py
        │   └── impl/
        │       └── SQLiteConnectionProvider.py
        ├── dao/                    # Data Access Object layer
        │   ├── __init__.py
        │   ├── AbstractDao.py
        │   ├── SQLiteDao.py
        │   └── impl/
        │       └── ArtistDao.py
        ├── factories/              # Factory pattern implementations
        │   ├── __init__.py
        │   ├── IDbFactory.py
        │   └── impl/
        │       ├── SQLiteDbFactory.py
        │       └── SQLiteRepositoryFactory.py
        ├── models/                 # Domain models
        │   ├── __init__.py
        │   └── Artist.py
        └── repositories/           # Repository pattern implementations
            ├── __init__.py
            ├── IRepository.py
            └── impl/
                └── ArtistRepository.py
```

## 🏗️ Architecture Overview

This project follows clean architecture principles with clear separation of concerns:

### 1. **Models Layer** (`db.models`)
- **`Artist.py`**: Domain model representing an artist entity
- Database-agnostic domain objects with validation and business logic
- Implements Python dataclasses for type safety and structure

### 2. **Data Access Layer** (`db.dao`)
- **`AbstractDao.py`**: Abstract base class defining common database operations
- **`SQLiteDao.py`**: SQLite-specific DAO implementation with connection management
- **`ArtistDao.py`**: Artist-specific database operations (CRUD operations)

### 3. **Repository Layer** (`db.repositories`)
- **`IRepository.py`**: Generic repository interface with type safety
- **`ArtistRepository.py`**: Domain-focused artist operations using domain models

### 4. **Connection Management** (`db.connection`)
- **`IDbConnectionProvider.py`**: Connection provider interface
- **`SQLiteConnectionProvider.py`**: SQLite connection management with resource cleanup

### 5. **Factory Pattern** (`db.factories`)
- **`IDbFactory.py`**: Factory interface for database components
- **`SQLiteDbFactory.py`**: DAO factory implementation
- **`SQLiteRepositoryFactory.py`**: Repository factory implementation

## ✨ Key Features

- **Clean Architecture**: Clear separation of concerns across multiple layers
- **SOLID Principles**: Interface segregation, dependency inversion, and single responsibility
- **Generic Repository Pattern**: Type-safe CRUD operations with domain models
- **Factory Pattern**: Easy instantiation and dependency management
- **Connection Management**: Automatic connection handling and resource cleanup
- **Thread Safety**: Built-in locking mechanisms for concurrent database access
- **Retry Logic**: Automatic retry for database lock scenarios
- **Verbose Logging**: Optional debug output for troubleshooting
- **Type Safety**: Extensive use of Python type hints and generics

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses built-in SQLite)

### Installation
1. Clone or download the project
2. Navigate to the project directory
3. Run the application:
   ```bash
   cd src
   python main.py
   ```

## 💡 Usage Examples

### 1. Direct DAO Usage (Low-level database operations)

```python
from db.connection.impl.SQLiteConnectionProvider import SQLiteConnectionProvider
from db.dao.impl.ArtistDao import ArtistDao

.....

# Initialize connection
connection_provider = SQLiteConnectionProvider("database/music.db")
connection = connection_provider.get_connection()

# Use DAO directly
artist_dao = ArtistDao(connection=connection, verbose=True)

# Create table if it doesn't exist
if not artist_dao.is_table_exist():
    artist_dao.create_table_artist()

# Example usage: Create a new artist (replace with actual data)
new_artist_id = artist_dao.insert(artist_name="New Artist")
if new_artist_id!=-1:
    print(f"New artist created with id {new_artist_id} \nRetrieving the artist...")
    artist = artist_dao.get_artist_by_id(artist_id=new_artist_id)
    if artist:
        print(f"New Artist ID: {artist[ArtistDao._field_id]}, Name: {artist[ArtistDao._field_name]}")
    else:
        print("Failed to retrieve the new artist.")

.....

# Close connection
connection.close()
```

### 2. Factory Pattern Usage (Simplified object creation)

```python
from db.factories.impl.SQLiteDbFactory import SQLiteDbFactory

# Initialize factory
factory = SQLiteDbFactory("database/music.db", verbose=True)

.....
# Use factory methods
# Example usage: Create a new artist (replace with actual data)
new_artist_id = artist_dao.insert(artist_name="New Artist")
if new_artist_id!=-1:
    print(f"New artist created with id {new_artist_id} \nRetrieving the artist...")
    artist = artist_dao.get_artist_by_id(artist_id=new_artist_id)
    if artist:
        print(f"New Artist ID: {artist[ArtistDao._field_id]}, Name: {artist[ArtistDao._field_name]}")
    else:
        print("Failed to retrieve the new artist.")
```

### 3. Repository Pattern Usage (Domain-focused operations)

```python
from db.factories.impl.SQLiteRepositoryFactory import SQLiteRepositoryFactory
from db.models.Artist import Artist

# Initialize repository factory
factory = SQLiteRepositoryFactory("database/music.db")
artist_repository = factory.get_artist_repository()

.....

# Use domain objects
artist = artist_repository.add(Artist(name="Repo Artist"))
if artist:
    print(f"Artist created successfully with ID: {artist.artist_id}, Name: {artist.name}")

.....

```

## 🗄️ Database Schema

The system automatically creates the following SQLite tables:

### Artists Table
```sql
CREATE TABLE "artists" (
    ArtistId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name NVARCHAR(120)
)
```

## 🎨 Design Patterns Implemented

- **Repository Pattern**: Domain-focused data access abstraction
- **Factory Pattern**: Object creation and dependency management
- **DAO Pattern**: Data access object for database operations
- **Strategy Pattern**: Pluggable database providers
- **Template Method**: Abstract base classes with common functionality
- **Dependency Injection**: Loose coupling between components

## 🔧 Extension Points

The architecture is designed for easy extension:

- **New Entities**: Add new models, DAOs, and repositories following existing patterns
- **Different Databases**: Implement new connection providers and DAO classes
- **Business Logic**: Add service layers above repositories
- **Caching**: Implement caching strategies in repository layer
- **Validation**: Add domain validation rules in model classes

## 📋 API Reference

### Artist Model
```python
@dataclass
class Artist:
    artist_id: int = None
    name: str = None
```

### Repository Interface
```python
class IRepository(Generic[T]):
    def add(self, entity: T) -> Optional[int]
    def get_by_id(self, entity_id: int) -> Optional[T]
    def update(self, entity: T) -> bool
    def delete(self, entity_id: int) -> bool
    def get_all(self) -> List[T]
```

### DAO Operations
```python
class ArtistDao:
    def insert(self, artist_name: str) -> int
    def get_artist_by_id(self, artist_id: int) -> dict
    def get_artist_by_name(self, artist_name: str) -> dict
    def get_all_artists(self) -> List[dict]
    def delete(self, artist_id: int) -> bool
    def create_table_artist(self) -> bool
```

## 🛠️ Development Guidelines

- Follow SOLID principles when adding new features
- Use type hints for better code documentation and IDE support
- Implement abstract methods when creating new database providers
- Add comprehensive error handling and logging
- Write unit tests for new components
- Follow the existing naming conventions and project structure

## 📝 License

This project is licensed under the Educational and Non-Commercial Use License.

## 👤 Author

**Alexandre Kavadias**

## 🎓 Educational Purpose

This project serves as an educational demonstration of:
- Clean architecture principles in Python
- Database design patterns implementation
- Type-safe programming with Python
- SOLID design principles
- Factory and Repository patterns
- SQLite database integration

Perfect for learning advanced Python programming concepts and database management system design.