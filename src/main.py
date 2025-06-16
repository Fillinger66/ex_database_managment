
from db.connection.impl.SQLiteConnectionProvider import SQLiteConnectionProvider
from db.dao.impl.ArtistDao import ArtistDao
from db.factories.impl.SQLiteDbFactory import SQLiteDbFactory
from db.repositories.impl.ArtistRepository import ArtistRepository
from db.models.Artist import Artist
from db.factories.impl.SQLiteRepositoryFactory import SQLiteRepositoryFactory


def dao_example():
     # Initialize the SQLite connection provider
    db_path = "database/music.db"  # Replace with your actual database path
    connection_provider = SQLiteConnectionProvider(database_path=db_path)

    # Get a new connection
    connection = connection_provider.get_connection()

    # Initialize the ArtistDao with the connection (dependency injection)
    artist_dao = ArtistDao(connection=connection, verbose=False)
   
    # Check if the artists table exists
    if not artist_dao.is_table_exist():
        print("Artists table does not exist. Creating table...")
        artist_dao.create_table_artist()
    else:
        print("Artists table already exists.")

    # Example usage: Get an artist by ID
    artist = artist_dao.get_artist_by_id(1)
    print(f"Retrieved artist: {artist["ArtistId"]}, {artist["Name"]}" if artist else "Artist not found.")

    input("Press Enter to continue...")  # Pause for user input

    # Example usage: Create a new artist (replace with actual data)
    new_artist_id = artist_dao.insert(artist_name="New Artist")
    if new_artist_id!=-1:
        print(f"New artist created with id {new_artist_id} \nRetrieving the artist...")
        artist = artist_dao.get_artist_by_id(artist_id=new_artist_id)
        if artist:
            print(f"New Artist ID: {artist[ArtistDao._field_id]}, Name: {artist[ArtistDao._field_name]}")
        else:
            print("Failed to retrieve the new artist.")

        input("Press Enter to continue...")  # Pause for user input

        affected_rows = artist_dao.update(artist_id=artist[ArtistDao._field_id], artist_name="Updated Artist Name")
        if affected_rows > 0:
            print("Artist updated successfully.")
            # Retrieve the updated artist
            updated_artist = artist_dao.get_artist_by_id(artist_id=artist[ArtistDao._field_id])
            if updated_artist:
                print(f"Updated Artist ID: {updated_artist[ArtistDao._field_id]}, Name: {updated_artist[ArtistDao._field_name]}")
            else:
                print("Failed to retrieve the updated artist.")
        else:
            print("Failed to update artist.")

        input("Press Enter to continue...")  # Pause for user input

        print("Deleting the new artist...")
        affected_rows = artist_dao.delete(artist_id=artist[ArtistDao._field_id])  # Example usage: delete an artist by ID (replace with a valid ID)
        if affected_rows > 0:
            print("Artist deleted successfully.")
        else:
            print("Failed to delete artist.")

    else:
        print("Failed to create new artist.")
    
    input("Press Enter to continue...")  # Pause for user input

    # Example usage: List all artists
    artists = artist_dao.get_all_artists()
    if not artists:
        print("No artists found.")
    else:
        for artist in artists:
            print(f"Artist ID: {artist[ArtistDao._field_id]}, Name: {artist[ArtistDao._field_name]}")
    
    # Close the connection when done
    connection.close()


def dao_factory_example():
    # Initialize the SQLiteDbFactory
    db_path = "database/music.db"  # Replace with your actual database path
    factory = SQLiteDbFactory(database_path=db_path, verbose=False)

    # Initialize the ArtistDao with the connection
    artist_dao = factory.get_artist_dao()

    # Check if the artists table exists
    if not artist_dao.is_table_exist():
        print("Artists table does not exist. Creating table...")
        artist_dao.create_table_artist()
    else:
        print("Artists table already exists.")

    # Example usage: Get an artist by ID
    artist = artist_dao.get_artist_by_id(1)
    print(f"Retrieved artist: {artist["ArtistId"]}, {artist["Name"]}" if artist else "Artist not found.")

    input("Press Enter to continue...")  # Pause for user input

    # Example usage: Create a new artist (replace with actual data)
    new_artist_id = artist_dao.insert(artist_name="New Artist")
    if new_artist_id!=-1:
        print(f"New artist created with id {new_artist_id} \nRetrieving the artist...")
        artist = artist_dao.get_artist_by_id(artist_id=new_artist_id)
        if artist:
            print(f"New Artist ID: {artist[ArtistDao._field_id]}, Name: {artist[ArtistDao._field_name]}")
        else:
            print("Failed to retrieve the new artist.")

        input("Press Enter to continue...")  # Pause for user input

        affected_rows = artist_dao.update(artist_id=artist[ArtistDao._field_id], artist_name="Updated Artist Name")
        if affected_rows > 0:
            print("Artist updated successfully.")
            # Retrieve the updated artist
            updated_artist = artist_dao.get_artist_by_id(artist_id=artist[ArtistDao._field_id])
            if updated_artist:
                print(f"Updated Artist ID: {updated_artist[ArtistDao._field_id]}, Name: {updated_artist[ArtistDao._field_name]}")
            else:
                print("Failed to retrieve the updated artist.")
        else:
            print("Failed to update artist.")

        input("Press Enter to continue...")  # Pause for user input

        print("Deleting the new artist...")
        affected_rows = artist_dao.delete(artist_id=artist[ArtistDao._field_id])  # Example usage: delete an artist by ID (replace with a valid ID)
        if affected_rows > 0:
            print("Artist deleted successfully.")
        else:
            print("Failed to delete artist.")

    else:
        print("Failed to create new artist.")
    
    input("Press Enter to continue...")  # Pause for user input

    # Example usage: List all artists
    artists = artist_dao.get_all_artists()
    if not artists:
        print("No artists found.")
    else:
        for artist in artists:
            print(f"Artist ID: {artist[ArtistDao._field_id]}, Name: {artist[ArtistDao._field_name]}")

def factory_as_facade_example():
    """
    This function demonstrates how to use the DAO factory as a facade.
    It initializes the SQLiteDbFactory and uses it to perform operations on the ArtistDao.
    """
    # Initialize the SQLiteDbFactory
    db_path = "database/music.db"  # Replace with your actual database path
    factory = SQLiteDbFactory(database_path=db_path, verbose=False)

    # Use the factory/facade to create an artist
    artist_id = factory.create_artist(artist_name="Facade Artist")

    if artist_id:
        print(f"Artist created successfully with ID: {artist_id}")

        input("Press Enter to continue...")  # Pause for user input

        # Retrieve the created artist
        artist = factory.get_artist_by_id(artist_id)
        if artist:
            print(f"Retrieved artist: {artist[ArtistDao._field_id]}, {artist[ArtistDao._field_name]}")
            # Update the artist's name
            affected_rows = factory.update_artist(artist_id, artist_name="Updated Facade Artist")
            if affected_rows > 0:
                print(f"Artist updated successfully.\nAffected rows: {affected_rows}")
                input("Press Enter to continue...")  # Pause for user input
                # Retrieve the updated artist
                updated_artist = factory.get_artist_by_id(artist_id)
                
                if updated_artist:
                    print(f"Updated Artist ID: {updated_artist[ArtistDao._field_id]}, Name: {updated_artist[ArtistDao._field_name]}")
                else:
                    print("Failed to retrieve the updated artist.")
                input("Press Enter to continue...")  # Pause for user input
            else:
                print("Failed to update artist.")

            print("Deleting the artist...")
            affected_rows = factory.delete_artist(artist_id)
            if affected_rows > 0:
                print(f"Artist deleted successfully.\nAffected rows: {affected_rows}")
            else:
                print("Failed to delete artist.")
            input("Press Enter to continue...")  # Pause for user input

    else:
        print("Failed to create artist.")

    # Retrieve the created artist
    artists = factory.get_all_artists()

    if artists:
        print("List of all artists:")
        for artist in artists:
            print(f"Artist ID: {artist[ArtistDao._field_id]}, Name: {artist[ArtistDao._field_name]}")
    else:
        print("No artist found.")
    
    input("Press Enter to continue...")  # Pause for user input

def repository_example():
    """
    This function demonstrates how to use the DAO factory as a facade.
    It initializes the SQLiteDbFactory and uses it to perform operations on the ArtistDao.
    """
    # Initialize the SQLiteDbFactory

    db_path = "database/music.db"  # Replace with your actual database path
    repository_factory = SQLiteRepositoryFactory(database_path=db_path, verbose=False)
    artist_repository = repository_factory.get_artist_repository()



    # Use the factory to create an artist
    print("Creating a new artist...")
     # Create a new artist
     
    artist = Artist(name="Repo Artist")
    artist = artist_repository.add(artist)
    if artist:
        print(f"Artist created successfully with ID: {artist.artist_id}, Name: {artist.name}")

        input("Press Enter to continue...")  # Pause for user input
        # Update the artist's name
        artist.name = "Updated Repo Artist"

        affected_rows = artist_repository.update(artist)
        if affected_rows:
            print(f"Artist updated successfully. Affected row: {affected_rows}")
            input("Press Enter to continue...")  # Pause for user input
            # Retrieve the updated artist
            updated_artist = artist_repository.get_by_id(artist.artist_id)
            if updated_artist:
                print(f"Updated Artist ID: {updated_artist.artist_id}, Name: {updated_artist.name}")
            else:
                print("Failed to retrieve the updated artist.")
            input("Press Enter to continue...")  # Pause for user input
            affected_rows = artist_repository.delete(artist.artist_id)
            # delete the artist
            if affected_rows:
                print("Artist deleted successfully.")
            else:
                print("Failed to delete artist.")

            input("Press Enter to continue...")  # Pause for user input
        else:
            print("Failed to update artist.")

    else:
        print("Failed to create artist.")

   
    artists = artist_repository.get_all()
    if not artists:
        print("No artists found.")
    else:
        for artist in artists:
            print(f"Artist ID: {artist.artist_id}, Name: {artist.name}")

    input("Press Enter to continue...")  # Pause for user input


def menu():
    print("1. Run DAO example")
    print("2. Run DAO factory example")
    print("3. Run DAO factory as facade example")
    print("4. Run repository example")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    while True:
        user_choice = menu()
        if user_choice == "1":
            print("Running DAO example...")
            dao_example()
        elif user_choice == "2":
            print("Running DAO factory example...")
            dao_factory_example()
        elif user_choice == "3":
            print("Running DAO factory as facade example...")
            factory_as_facade_example()
        elif user_choice == "4":
            print("Running repository example...")
            repository_example()
        elif user_choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")



