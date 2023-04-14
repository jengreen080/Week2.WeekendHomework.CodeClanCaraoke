import unittest
from src.room import Room
# from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.bowie_room = Room("Bowie", 12)
        self.queen_room = Room("Queen", 10)
        self.elton_room = Room("Elton", 4)

    def test_check_room_name(self):
        self.assertEqual("Bowie", self.bowie_room.room_name) #passes

    def test_add_guest_to_room(self):
        self.assertEqual(1, self.add_guest_to_room(second_guest))
        ### this is where we're at
