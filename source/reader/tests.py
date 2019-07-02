"""
    Testing the folder
"""
import os
import unittest

from source import ROOT_DIR
from source.reader.file import file_to_str, str_to_file
from source.reader.get_content import get_content
from source.reader.get_folder import get_folder_of_file


class MyTestCase(unittest.TestCase):
    def test_str_to_file(self):
        test_path = ROOT_DIR + "/delete.html"
        content = "test"
        str_to_file(test_path, content)
        new_content = file_to_str(test_path)
        self.assertEqual(new_content, content)
        os.remove(test_path)

        test_path = ROOT_DIR + "/fake/"
        # noinspection PyTypeChecker
        with self.assertRaises(SystemExit) as cm:
            content = "test"
            str_to_file(test_path, content)

        # noinspection PyUnresolvedReferences
        self.assertEqual(cm.exception.code, 1)

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

        self.assertEqual(file_to_str(test_path, False), None)

    def test_path(self):
        folder = ROOT_DIR + "/html_tests"
        test_path = folder + "/test.html"
        folder_result = get_folder_of_file(test_path)
        self.assertEqual(folder, folder_result)

        folder = "html_tests"
        test_path = folder + "/test.html"
        folder_result = get_folder_of_file(test_path)
        self.assertEqual(folder, folder_result)

    def test_get_content(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        js_path = root_dir + "/js/test.j"
        content = get_content(js_path, root_dir)
        self.assertEqual(content, None)
        js_path = root_dir + "/js/test.js"
        content = get_content(js_path, root_dir)
        self.assertNotEqual(content, None)
        js_path = "js/test.j"
        content = get_content(js_path, root_dir)
        self.assertEqual(content, None)

        js_path = "js/test.js"
        content = get_content(js_path, root_dir)
        self.assertNotEqual(content, None)
