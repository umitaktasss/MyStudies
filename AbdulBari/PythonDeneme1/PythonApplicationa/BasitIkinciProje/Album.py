import sqlite3
import time

class Song():
    
    def __init__(self, song_name, band_name, album, establish_date, time):
        self.song_name = song_name
        self.band_name = band_name
        self.album = album
        self.establish_date = establish_date
        self.time = time
        
    def __str__(self):
        return "Song: {}\nBand: {}\nAlbum: {}\nEstablished Date: {}\nDuration: {}".format(
            self.song_name, self.band_name, self.album, self.establish_date, self.time)


class ListA():
    def __init__(self):
        self.make_connection()
    
    def make_connection(self):
        self.connection = sqlite3.connect(r"C:\Users\Tulpar\Desktop\Algorithm\AbdulBari\AbdulBari\PythonDeneme1\PythonApplicationa\song_collection.db")

        self.cursor = self.connection.cursor()
        
        thing = "CREATE TABLE IF NOT EXISTS Songs (Song TEXT, Band TEXT, Album TEXT, Established_Date TEXT, Duration INT)"
        self.cursor.execute(thing)
        self.connection.commit()
        
    def cut_connection(self):
        self.connection.close()
        
    def show_allist(self):
        thing = "SELECT * FROM Songs"
        self.cursor.execute(thing)
        songs = self.cursor.fetchall()
        if len(songs) == 0:
            print("The list is empty...")
        else:
            for i in songs:
                print("*************************************************************")
                song = Song(i[0], i[1], i[2], i[3], i[4])
                print(song)

    def add_song(self, song):
        ask = "INSERT INTO Songs (Song, Band, Album, Established_Date, Duration) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(ask, (song.song_name, song.band_name, song.album, song.establish_date, song.time))
        self.connection.commit()
        print(f"Song '{song.song_name}' has been added to the database.")
    
    def delete_song(self, song_name):
        # Check if song exists
        ask = "SELECT * FROM Songs WHERE Song = ?"
        self.cursor.execute(ask, (song_name,))
        song = self.cursor.fetchone()
        
        if song:
            # Song exists, delete it
            ask = "DELETE FROM Songs WHERE Song = ?"
            self.cursor.execute(ask, (song_name,))
            self.connection.commit()
            print(f"Song '{song_name}' has been deleted.")
        else:
            # Song does not exist
            print(f"Warning: Song '{song_name}' does not exist in the database.")

    def update_song(self, song_name, new_band=None, new_album=None, new_date=None, new_duration=None):
        # Check if song exists
        ask = "SELECT * FROM Songs WHERE Song = ?"
        self.cursor.execute(ask, (song_name,))
        song = self.cursor.fetchone()
        
        if song:
            # Song exists, perform updates based on what is provided
            if new_band:
                ask = "UPDATE Songs SET Band = ? WHERE Song = ?"
                self.cursor.execute(ask, (new_band, song_name))
            if new_album:
                ask = "UPDATE Songs SET Album = ? WHERE Song = ?"
                self.cursor.execute(ask, (new_album, song_name))
            if new_date:
                ask = "UPDATE Songs SET Established_Date = ? WHERE Song = ?"
                self.cursor.execute(ask, (new_date, song_name))
            if new_duration:
                ask = "UPDATE Songs SET Duration = ? WHERE Song = ?"
                self.cursor.execute(ask, (new_duration, song_name))

            self.connection.commit()
            print(f"Song '{song_name}' has been updated.")
        else:
            print(f"Warning: Song '{song_name}' does not exist in the database.")

    def total_duration(self):
        ask = "SELECT SUM(Duration) FROM Songs"
        self.cursor.execute(ask)
        total = self.cursor.fetchone()[0]
        
        if total:
            print(f"Total duration of all songs: {total} minutes")
        else:
            print("No songs in the database to calculate total duration.")

    def show_song(self, song_name):
        ask = "SELECT * FROM Songs WHERE Song = ?"
        self.cursor.execute(ask, (song_name,))
        song = self.cursor.fetchone()
        
        if song:
            # Convert the fetched data into a Song object and print it
            found_song = Song(song[0], song[1], song[2], song[3], song[4])
            print(found_song)
        else:
            print(f"Warning: Song '{song_name}' does not exist in the database.")