import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    
   #  setup
    def setUp(self):
       
       self.song_1 = Song("Doomsday", "Architects")
       self.song_2 = Song("Afterlife", "Avenged Sevenfold")
       self.song_3 = Song("Sleep Token", "Alkaline")

   # test song has a title  
    def test_song_has_title(self):
        self.assertEqual("Doomsday", self.song_1.title)

   # test song has an artist 
    def test_song_has_artist(self):
        self.assertEqual("Avenged Sevenfold", self.song_2.artist)

