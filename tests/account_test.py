import unittest
from src.account import *
from src.profile import *

class TestAccount(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")

        self.account_1 = Account("Jane", "Smith", "janes@email.com")

    # Test an Account can add a Profile
    def test_account_can_add_profile(self):
        self.account_1.add_profile(self.profile_1)
        self.assertEqual(1, len(self.account_1.profiles))

    # # Test an Account can remove a given Profile
    def test_account_can_remove_profile(self):
        self.account_1.profiles = [(self.profile_1), (self.profile_2)]
        self.account_1.remove_profile(self.profile_2)
        self.assertEqual(1, len(self.account_1.profiles))

    # # # Test an Account can return a list of Profiles
    def test_account_can_return_list_of_profiles(self):
        self.account_1.add_profile(self.profile_1)
        self.account_1.add_profile(self.profile_2)
        self.assertEqual(["harrisonF", "markH"], self.account_1.get_profiles())