"""
    Testing the folder
"""
import unittest

from source import ROOT_DIR
from source.internet.download import download_from_link
from source.reader.file import file_to_str


class MyTestCase(unittest.TestCase):

    def test_download(self):
        path_root = ROOT_DIR + "/html_tests/css/test.css"
        self.assertEqual(None, download_from_link("test"))
        self.assertEqual(None, download_from_link(
            "https://thisIsAFake12345684235815105.eu/file"
        ))
        content = file_to_str(path_root)
        self.assertEqual(content, download_from_link("file:///" + path_root))
