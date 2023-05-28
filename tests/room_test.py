import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    # setup
    def setUp(self):
        
        self.room = Room("The Boiler Room", 10, 20)

        self.guest_1 = Guest("Paul", 100, "Doomsday")
        self.guest_2 = Guest("Heather", 100, "Alkaline")

        self.song_1 = Song("Doomsday", "Architects")
        self.song_2 = Song("Afterlife", "Avenged Sevenfold")
        self.song_3 = Song("Alkaline", "Sleep Token")

    # test room has a name 
    def test_room_has_name(self):
        self.assertEqual("The Boiler Room", self.room.room_name)

    # test room has a capacity 
    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)

    # test room has an entry fee 
    def test_room_has_entry_fee(self):
        self.assertEqual(20, self.room.entry_fee)

    # test when a guest checks in
    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_2)
        self.assertEqual([self.guest_2], self.room.guests)

    # test when a guest checks out 
    def test_check_out_guest(self):
        self.room.check_out_guest(self.guest_2)
        self.assertEqual([], self.room.guests)

    # test when a song is added to a room
    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song_2)
        self.assertEqual([self.song_2], self.room.songs)
