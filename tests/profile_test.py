import unittest
from src.profile import *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)

        self.profile_1 = Profile("harrisonF", "myP@assword")

    # Test a Profile can add a favourite Movie
    def test_profile_can_add_fave_movie(self):
        self.profile_1.add_fave_movie(self.movie_1)
        self.assertEqual(1, len(self.profile_1.favourites)

    # Test a Profile can remove a given Movie from favourites
    def test_profile_can_remove_fave_movie(self):
        self.profile_1.remove_fave_movie(self.movie)

    # # Test a Profile can return a list of Favourites
    def test_profile_can_return_list_of_faves(self):
        self.profile_1.add_fave_movie(self.movie_1)
        self.assertEqual([('Hunger Games', 'Gary Ross')], self.profile_1.get_faves(self.profile_1))