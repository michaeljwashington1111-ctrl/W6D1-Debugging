import unittest, reverser

class TestReverser(unittest.TestCase):
    def test_reverse_basic(self):
        self.assertEqual(reverser.reverse_string("hello"), "olleh")

    def test_reverse_empty(self):
        self.assertEqual(reverser.reverse_string(""), "")

    def test_reverse_spaces(self):
        self.assertEqual(reverser.reverse_string("a b"), "b a")

    def test_reverse_single_char(self):
        self.assertEqual(reverser.reverse_string("Z"), "Z")

if __name__ == "__main__":
    unittest.main(verbosity=2)
