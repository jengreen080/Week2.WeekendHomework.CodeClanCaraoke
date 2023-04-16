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
        # How could I set up a class to input straight into a dictionary?

        # self.guest_dictionary = {self.first_guest.guest_name : self.first_guest.guest_age, 
        #     self.second_guest.guest_name : self.second_guest.guest_age,
        #     self.third_guest.guest_name : self.third_guest.guest_age,
        #     self.forth_guest.guest_name : self.forth_guest.guest_age,
        #     self.fith_guest.guest_name : self.fith_guest.guest_age}

    # def test_return_guest(self):
    #     self.assertEqual("Sam", list(self.guest_dictionary.keys())[2]) #passes
