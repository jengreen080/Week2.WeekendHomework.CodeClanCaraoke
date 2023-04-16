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

    def test_check_room_name(self):
        self.assertEqual("Bowie", self.bowie_room.room_name) #passes

    def test_add_guest_to_room(self):
        # print(self.room_list_of_people_within_room)
        # print(self.bowie_room.room_number_of_people_in_room)
        number_of_people_in_room = self.bowie_room.add_guest_to_room(self.first_guest)
        number_of_people_in_room = self.bowie_room.add_guest_to_room(self.second_guest)
        self.assertEqual(2, number_of_people_in_room) 
        # print(self.bowie_room.room_list_of_people_within_room)


    #### How can i see if my code works when referring to an 'entire' guest, not just name/age etc.?

    def test_remove_guest_from_room(self):
        self.room_list_of_people_within_room = [self.first_guest.guest_name, self.second_guest.guest_name, self.third_guest.guest_name, self.forth_guest.guest_name, self.fifth_guest.guest_name]
        # print(self.room_list_of_people_within_room)
        number_of_people_in_room = self.bowie_room.remove_guest_from_room(self.first_guest.guest_name)
        return number_of_people_in_room
        self.assertEqual(4, number_of_people_in_room)
        print(number_of_people_in_room)
        print(self.room_list_of_people_within_room)
        ## why has my code greyed itself out? Test seems to be running

    def test_add_song_to_room(self):
        self.test_add_song_to_room(self.song1.song_name)
        ## why is the above line saying i'm giving in 2 positional arguemnts? I'm baffled. Not currently running
        self.assertEqual(1, len(self.bowie_room.room_song_list))