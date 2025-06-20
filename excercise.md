# Excercise

In this excercise, you will be asked to integrate 2 others tables in the project by implementing DAOs, Factory, repositories and entity class (model).
That will show you the split of responsability as each part do its own job.

## First step

**Create DAOs for tables** : 
- **Playlist**
- **Tracks**

The DAO is responsible to query the database nothing more.

These tables are linked through ```playlist_track``` table, so keep this in mind during the query elaboration

**Use structured query to have a protection against SQL injection**
```python
return self.execute_query(query= 
                                 f"""
                                SELECT {self._field_id}, {self._field_name}
                                FROM {self.tablename}
                                WHERE {self._field_id} = ?
                                """, 
                                params=(artist_id,), 
                                fetch_one=True, 
                                fetch_all=False)
```

As you see above, the query and parameters are separated. This is the good practice to avoid SQL injection.


### How to create DAO

1. Create a class file ```src/db/dao/impl/[Tablename]Dao.py``` (eg. ```TrackDao.py```)
2. The class have to extends ```src/db/dao/SQLiteDao.py```
3. Define the database columns name and tablename as variables of your class
4. Define ```def create_table_[tablename]``` method that will return the create table query
3. Add different method like in ```ArtistDao``` class
    - insert
    - update
    - delete
    - get_all
    - get_by_id
4. Create a function in the file ```main.py``` to test and validate your class

***Tips :***
 - *Use a Db Browser to elaborate and test yours queries before doing it in python*
 - *Check out ArtistDao and how it uses ```SQLiteDao``` methods to query database*

## Second step : 

Update the ```SQLiteDbFactory.py``` to add functions that will handle the creation of your newly created DAO ```main.py```

Take a look at the creation of ```ArtistDao``` to create function for your DAO

## Thrid step : 

Create yours Entities class (```Track.py``` & ```Playlist.py```) to be able to use them with repository
Create classes representing a row for each tables. See ```src/db/models/Artist.py```

Example : 
```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Artist:
    """
    Represents a user from Table users.
    """
    artist_id: int = field(default=None) # Use default=None for fields that might be auto-generated by DB
    name: str = field(default=None)
    ....
```

The table **Playlist** is **linked** to **Tracks** table thanks to the **relation table ``` playlist_track ```**

**In this case, the relation table doesn't not have to be created as a python class as it's only used to link tables**

***Remark : Be careful with relation table, sometimes it can contain revelant fields so you will need to handle it differently***

So for the ```class Playlist```, you will need to add a list of ```Track```.

***Tips : When you will create the Playlist object and populate it, build first the Playlist object and then fetch all tracks related to the playlist and build the list to feed the Playlist object.***

Example : 

Full object creation

1. Fetch the playlist and create the object
2. Fetch all tracks for the playlist, create each track object and add it to the list of track in the playlist object

Lazy loading (Create only Playlist object and load tracks when you need it)

1. Fetch the playlist and populate the Playlist object
2. Later when you need tracks related to this Playlist, populate it


# Fourth step

Now you have DAOs and the object reflecting database table (Entity class), you can start creating repositories. **You will have to create a repository per table**

The repository is responsible to fetch data from database thanks to yours DAOs and create the right entity to return.

To create the repository you have to : 
1. Create a new class ```src/db/repository/impl/[tablename]Repository.py```
2. Extends the ```src/db/repository/IRepository.py```
3. Implements all the method from IRepository
4. Test the repository in ```main.py```



# Fifth step

Now you have the repositories done, let's adapt the ```src/db/factory/impl/SQLiteRepositoryFactory.py``` to add these news repositories

The factory is responsible to create the database connection, inject it to the repository and return it

Example : 

```python
def get_artist_repository(self) -> ArtistRepository:
        """Get an ArtistRepository with a new connection."""
        return ArtistRepository(connection=self.get_connection(), verbose=self.verbose)
```




