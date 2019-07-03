# coding=utf-8
"""
    test the images functions
"""
import os
import unittest

from source import ROOT_DIR
from source.img.convert import path_to_bin
from source.img.get_img import get_image
from source.reader.file import file_to_str

EXTENSIONS = ["bmp", "gif", "jpg", "ico", "png"]


class MyTestCase(unittest.TestCase):
    def test_convert(self):
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

    def test_get_img(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        img_path = root_dir + "/img/tiny.j"
        content = get_image(img_path, root_dir)
        self.assertEqual(content, None)
        img_path = root_dir + "/img/tiny.png"
        content = get_image(img_path, root_dir)
        self.assertNotEqual(content, None)
        img_path = "img/tiny.pn"
        content = get_image(img_path, root_dir)
        self.assertEqual(content, None)

        img_path = "img/tiny.png"
        content = get_image(img_path, root_dir)
        self.assertNotEqual(content, None)
