import random
import unittest

class TestStuff(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
        
    def test_choice2(self):
        element = 11
        self.assertFalse(element in self.seq)

if __name__ == '__main__':
    unittest.main()
