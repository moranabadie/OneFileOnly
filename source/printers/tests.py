"""
    testing the folder
"""
import sys
import unittest

from source.printers.help import show_help, SHOW_MESSAGE
from source.printers.wrong_arg import print_wrong_argument, WRONG_ARG_MESSAGE

if sys.version_info[0] < 3:  # pragma: no cover
    from io import BytesIO as StringIO
else:
    from io import StringIO


class MyTestCase(unittest.TestCase):
    def test_all(self):
        before = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        show_help()
        self.assertTrue(SHOW_MESSAGE in captured_output.getvalue())
        print_wrong_argument()
        self.assertTrue(WRONG_ARG_MESSAGE in captured_output.getvalue())
        sys.stdout = before
