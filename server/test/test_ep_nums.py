import unittest

from app.utils import abs_ep_num, FAKE_DB

class TestEpisodeNumbers(unittest.TestCase):
    def setUp(self):
        self.fake_db = FAKE_DB

    def test_pilot_ep(self):
        self.assertEqual(abs_ep_num(self.fake_db, "Suits", 1, 1), 1)

    def test_s2e4_suits(self):
        self.assertEqual(abs_ep_num(self.fake_db, "Suits", 2, 4), 16)

    def test_s6e14_suits(self):
        self.assertEqual(abs_ep_num(self.fake_db, "Suits", 6, 14), 90)

if __name__ == '__main__':
    unittest.main()