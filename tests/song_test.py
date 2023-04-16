import unittest
from src.song import Song
# from src.guest import Guest
# from src.room import Room

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_greenday = Song("Greenday", "American Idiot")
        self.song_taylor_swift = Song("Taylor Swift", "...Ready For It?")
        self. song_busted = Song("Busted", "Shipwrecked in Atlantis")

    def test_check_song_artist(self):
        self.assertEqual("Busted", self.song_busted.song_artist) #passes