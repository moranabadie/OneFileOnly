"""
    Testing the folder
"""
import unittest

from source import ROOT_DIR
from source.reader.file import file_to_str


class MyTestCase(unittest.TestCase):
    def test_read_file(self):
        test_path = ROOT_DIR + "/html_tests/test.html"
        file_to_str(test_path)
        test_path = ROOT_DIR + "/html_tests/tes.html"
        # noinspection PyTypeChecker
        with self.assertRaises(SystemExit) as cm:
            file_to_str(test_path)

        # noinspection PyUnresolvedReferences
        self.assertEqual(cm.exception.code, 1)
