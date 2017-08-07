import unittest

import awesome

import os
class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
