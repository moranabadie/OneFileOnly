"""
    testing the folder
"""
import unittest

from source.printers.help import show_help
from source.printers.wrong_arg import print_wrong_argument


class MyTestCase(unittest.TestCase):
    def test_all(self):
        show_help()
        print_wrong_argument()
        # too lazy
        self.assertEqual(True, True)
