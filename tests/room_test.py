import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        
        self.room = Room("The Boiler Room", 15, 35)

        self.guest_1 = Guest("Paul", 100, "Doomsday")
        self.guest_2 = Guest("Heather", 100, "Alkaline")

        self.song_1 = Song("Doomsday", "Architects")
        self.song_2 = Song("Afterlife", "Avenged Sevenfold")
        self.song_3 = Song("Alkaline", "Sleep Token")


    # def test_room_has_name(self):
    #     self.assertEqual("The Boiler Room", self.room.room_name)


    # def test_room_has_capacity(self):
    #     self.assertEqual(10, self.room.capacity)


    # def test_room_has_entry_fee(self):
    #     self.assertEqual(20, self.room.entry_fee)


    # def test_check_in_guest(self):
    #     self.room.check_in_guest(self.guest_2)
    #     self.assertEqual([self.guest_2], self.room.guests)


    # def test_check_out_guest(self):
    #     self.room.check_out_guest(self.guest_2)
    #     self.assertEqual([], self.room.guests)


    # def test_add_song_to_room(self):
    #     self.room.add_song_to_room(self.song_2)
    #     self.assertEqual([self.song_2], self.room.songs)