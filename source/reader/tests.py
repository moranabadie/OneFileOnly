"""
    Testing the folder
"""
import unittest

from source import ROOT_DIR
from source.reader.file import file_to_str
from source.reader.get_folder import get_folder_of_file


class MyTestCase(unittest.TestCase):
    def test_read_file(self):
        test_path = ROOT_DIR + "/html_tests/test.html"
        content = file_to_str(test_path)
        self.assertTrue("<!DOCTYPE html>" in content)

        test_path = ROOT_DIR + "/html_tests/tes.html"
        # noinspection PyTypeChecker
        with self.assertRaises(SystemExit) as cm:
            file_to_str(test_path)

        # noinspection PyUnresolvedReferences
        self.assertEqual(cm.exception.code, 1)

    def test_path(self):
        folder = ROOT_DIR + "/html_tests"
        test_path = folder + "/test.html"
        folder_result = get_folder_of_file(test_path)
        self.assertEqual(folder, folder_result)

        folder = "html_tests"
        test_path = folder + "/test.html"
        folder_result = get_folder_of_file(test_path)
        self.assertEqual(folder, folder_result)
