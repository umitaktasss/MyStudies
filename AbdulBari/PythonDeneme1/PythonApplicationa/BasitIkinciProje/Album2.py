from Album import *

print("""**************************************************
 Welcome to the Music Library Program.

 Operations:
 1- Show All Songs
 2- Search for a Song
 3- Add a Song
 4- Delete a Song
 5- Update a Song
    
 Press '*' to exit.
************************************************** """)

music_library = ListA()

while True:
    operation = input("Select an operation: ")
    
    if operation == '*':
        print("Exiting the program...")
        music_library.cut_connection()  # Close the database connection
        break
    
    elif operation == '1':
        music_library.show_allist()
        
    elif operation == '2':
        song_name = input("Which song are you looking for? ")
        print("Searching for the song...")
        time.sleep(2)
        music_library.show_song(song_name)  # Assuming show_song method searches and shows the song
        
    elif operation == '3':
        song_name = input("Song Name: ")
        band_name = input("Band Name: ")
        album = input("Album: ")
        establish_date = input("Established Date: ")
        duration = int(input("Duration (in minutes): "))
        
        new_song = Song(song_name, band_name, album, establish_date, duration)
        
        print("Adding the song...")
        time.sleep(2)
        
        music_library.add_song(new_song)
        print("Your operation was successful!")
        
    elif operation == '4':
        song_name = input("Which song do you want to delete? ")
        
        confirm = input("Are you sure you want to delete this song? (Y / N): ")
        if confirm.upper() == 'Y':
            print("Deleting the song...")
            time.sleep(2)
            music_library.delete_song(song_name)
            print("Your operation was successful!")
        elif confirm.upper() == 'N':
            pass
        else:
            print("Invalid input!")
            
    elif operation == '5':
        song_name = input("Which song would you like to update? ")

        print("""
        What would you like to update?
        1- Song Name
        2- Band Name
        3- Album
        4- Established Date
        5- Duration
        """)

        update_choice = input("Select the number of the field to update: ")

        if update_choice == '1':
            new_name = input("Enter the new song name: ")
            print("Updating song name...")
            time.sleep(2)
            music_library.update_song(song_name, new_song_name=new_name)
            print("Song name updated successfully!")

        elif update_choice == '2':
            new_band = input("Enter the new band name: ")
            print("Updating band name...")
            time.sleep(2)
            music_library.update_song(song_name, new_band=new_band)
            print("Band name updated successfully!")

        elif update_choice == '3':
            new_album = input("Enter the new album name: ")
            print("Updating album...")
            time.sleep(2)
            music_library.update_song(song_name, new_album=new_album)
            print("Album updated successfully!")

        elif update_choice == '4':
            new_date = input("Enter the new established date: ")
            print("Updating established date...")
            time.sleep(2)
            music_library.update_song(song_name, new_establish_date=new_date)
            print("Established date updated successfully!")

        elif update_choice == '5':
            new_duration = int(input("Enter the new duration (in minutes): "))
            print("Updating duration...")
            time.sleep(2)
            music_library.update_song(song_name, new_duration=new_duration)
            print("Duration updated successfully!")

        else:
            print("Invalid choice! Please select a valid option.")
        
    else:
        print("Invalid operation!")
