# coding=utf-8
"""
    test the images functions
"""
import unittest

from source import ROOT_DIR
from source.img.convert import path_to_bin
from source.reader.file import file_to_str

EXTENSIONS = ["bmp", "gif", "jpg", "ico", "png"]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        path_root = ROOT_DIR + "/html_tests/img/not_exists.bmp"
        content = path_to_bin(path_root)
        self.assertEqual(content, None)
        path_root = ROOT_DIR + "/html_tests/img/tiny"
        content = path_to_bin(path_root)
        self.assertEqual(content, None)
        for ext in EXTENSIONS:
            path_root = ROOT_DIR + "/html_tests/img/tiny." + ext

            right_answer = file_to_str(ROOT_DIR + "/html_tests/img/" + ext + ".txt")
            content = path_to_bin(path_root)
            self.assertEqual(right_answer, content)
