"""
    Test the folder
"""
import sys
import unittest
from io import StringIO

from source import ROOT_DIR
from source.arguments import HELPERS
from source.arguments.caller import call_function
from source.printers.help import SHOW_MESSAGE
from source.printers.wrong_arg import AN_ERROR


class MyTestCase(unittest.TestCase):
    def test_caller(self):
        for h in HELPERS:
            before = sys.stdout
            captured_output = StringIO()
            sys.stdout = captured_output
            call_function(h)
            self.assertTrue(SHOW_MESSAGE in captured_output.getvalue())
            sys.stdout = before

        command = "/home/sys/file.htm"
        before = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        call_function(command)
        self.assertTrue(AN_ERROR in captured_output.getvalue())
        sys.stdout = before

        command = ROOT_DIR + "/html_tests/test.html"
        before = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        call_function(command)
        self.assertTrue(AN_ERROR not in captured_output.getvalue())
        sys.stdout = before
