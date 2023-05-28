import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    # setup
    def setUp(self):
        self.guest_1 = Guest("Paul", 100, "Doomsday")
        self.guest_2 = Guest("Heather", 100, "Alkaline")
        
    # test guest has the same name
    def test_guest_has_name(self):
        self.assertEqual("Paul", self.guest_1.guest_name)

    # test guest has enough money
    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_1.guest_money)

    # test guest has a favourite song
    def test_guest_has_favorite_song(self):
        self.assertEqual("Alkaline", self.guest_2.favourite_song)

