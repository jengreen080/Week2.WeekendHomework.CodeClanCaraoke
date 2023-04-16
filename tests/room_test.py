import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.bowie_room = Room("Bowie", 12)
        self.queen_room = Room("Queen", 10)
        self.elton_room = Room("Elton", 4)
        self.first_guest = Guest("Marnie", 26)
        self.second_guest = Guest("Kathrine", 30)
        self.third_guest = Guest("Sam", 28)
        self.forth_guest = Guest("Adam", 25)
        self.fifth_guest = Guest("Alan", 28)
        self.song1 = Song("Busted", "Shipwrecked in Atlantis")

        self.room_list_of_people_within_room = {1 : [self.first_guest.guest_name, self.first_guest.guest_age],
                                                2 : [self.second_guest.guest_name, self.second_guest.guest_age],
                                                3 : [self.third_guest.guest_name, self.third_guest.guest_age],
                                                4 : [self.forth_guest.guest_name, self.forth_guest.guest_age],
                                                5 : [self.fifth_guest.guest_name, self.fifth_guest.guest_age]}

    # def test_check_room_name(self):
    #     self.assertEqual("Bowie", self.bowie_room.room_name) #passes

    # I find it hard to know what I need to define in setUp. If I've defined my guests in guest_test

    def test_add_guest_to_room(self):
        print(self.room_list_of_people_within_room)
        print(self.bowie_room.room_number_of_people_in_room)
        number_of_people_in_room = self.bowie_room.add_guest_to_room(self.first_guest)
        number_of_people_in_room = self.bowie_room.add_guest_to_room(self.second_guest)
        self.assertEqual(2, number_of_people_in_room) 
        print(self.bowie_room.room_list_of_people_within_room)


    #### so confused here

    # def test_remove_guest_from_room(self):
    #     self.room_list_of_people_within_room = [self.first_guest, self.second_guest, self.third_guest, self.forth_guest, self.fifth_guest]
    #     print(self.room_list_of_people_within_room)
    #     number_of_people_in_room = self.bowie_room.remove_guest_from_room(self.first_guest)
    #     print(self.room_list_of_people_within_room)
    #     self.assertEqual(4, number_of_people_in_room)
    
    # how woul I check to make sure the person is in the list?
    # def check_name_of_person_in_room(self):
    #     self.assertEqual(, self.bowie_room.Guest)

    # def test_add_song_to_room(self):
    #     self.test_add_song_to_room(song1)
    #     self.assertEqual(1, len(self.bowie_room.room_song_list))