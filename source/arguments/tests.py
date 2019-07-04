# coding=utf-8
"""
    Test the folder
"""
import os
import sys
import unittest

from source import ROOT_DIR
from source.arguments import HELPERS
from source.arguments.caller import call_function
from source.printers.help import SHOW_MESSAGE
from source.printers.wrong_arg import AN_ERROR

if sys.version_info[0] < 3:  # pragma: no cover
    from io import BytesIO as StringIO
else:
    from io import StringIO


class MyTestCase(unittest.TestCase):
    def test_caller(self):
        for h in HELPERS:
            before = sys.stdout
            captured_output = StringIO()
            sys.stdout = captured_output
            call_function([h])
            self.assertTrue(SHOW_MESSAGE in captured_output.getvalue())
            sys.stdout = before

        command = "/home/sys/file.htm"
        before = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        call_function([command])
        self.assertTrue(AN_ERROR in captured_output.getvalue())
        sys.stdout = before

        command = ROOT_DIR + "/html_tests/test.html"
        before = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        call_function([command])
        self.assertTrue(AN_ERROR not in captured_output.getvalue())
        sys.stdout = before

        self.assertTrue(os.path.isfile(ROOT_DIR + "/../one_file.html"))
        os.remove(ROOT_DIR + "/../one_file.html")

        command = ROOT_DIR + "/html_tests/test.html"
        before = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        call_function([command])
        self.assertTrue(AN_ERROR not in captured_output.getvalue())
        sys.stdout = before

        self.assertTrue(os.path.isfile(ROOT_DIR + "/../one_file.html"))
        os.remove(ROOT_DIR + "/../one_file.html")

        command = ROOT_DIR + "/html_tests/test.html"
        command2 = ROOT_DIR + "/../delete.html"
        before = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        call_function([command, command2])
        self.assertTrue(AN_ERROR not in captured_output.getvalue())
        sys.stdout = before

        self.assertTrue(os.path.isfile(ROOT_DIR + "/../delete.html"))
        os.remove(ROOT_DIR + "/../delete.html")
