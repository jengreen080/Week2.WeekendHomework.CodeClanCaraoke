import unittest
from src.guest import Guest
# from src.song import Song
# from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.first_guest = Guest("Marnie", 26)
        self.second_guest = Guest("Kathrine", 30)
        self.third_guest = Guest("Sam", 28)
        self.forth_guest = Guest("Adam", 25)
        self.fith_guest = Guest("Alan", 28)

    def test_return_guest(self):
        self.assertEqual(25 , self.forth_guest.guest_age) #passes