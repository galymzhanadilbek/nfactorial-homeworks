# tests/test_ascii_generator.py

import unittest
from src.ascii_generator import generate_ascii_art

class TestAsciiGenerator(unittest.TestCase):
    def test_generate_ascii_art(self):
        result = generate_ascii_art("hello")
        self.assertEqual(result, "HELLO")

if __name__ == "__main__":
    unittest.main()
