class Room:
    
    def __init__(self, name, capacity):
        self.room_name = name
        self.room_capacity = capacity
        # self.room_list_of_people_within_room = {}
        self.room_list_of_people_within_room = []
        self.room_number_of_people_in_room = 0
        self.room_song_list = []

    def add_guest_to_room(self, guest):
        if self.room_capacity > len(self.room_list_of_people_within_room):
            self.room_list_of_people_within_room.append(guest)

            # self.room_list_of_people_within_room.update({index:guest})
            self.room_number_of_people_in_room += 1
            return self.room_number_of_people_in_room
    
    def remove_guest_from_room(self, guest):
        if len(self.room_list_of_people_within_room) > 0 :
            self.room_list_of_people_within_room.remove(guest)
            self.room_number_of_people_in_room -= 1
            return self.room_number_of_people_in_room


    def add_song_to_room(self, song):
            self.room_song_list = self.room_song_list.append(song)


        
        