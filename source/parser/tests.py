"""
    Testing the folder
"""
import unittest

from source import ROOT_DIR
from source.parser.replace_js import _right_script, _src_parser, _SCRIPT_SPLIT


class MyTestCase(unittest.TestCase):
    def test_replace_js(self):
        root_dir = ROOT_DIR + "/source/html_tests/"
        code = ' src=js/test.js>'
        new_code = _src_parser(code, ('src="', '"'), root_dir)
        self.assertEqual(new_code, _SCRIPT_SPLIT + code)
        code = ' src="js/test.js\'>'
        new_code = _src_parser(code, ('src="', '"'), root_dir)
        self.assertEqual(new_code, _SCRIPT_SPLIT + code)

        code = ' src="js/test.js">'
        new_code = _src_parser(code, ('src="', '"'), root_dir)
        self.assertNotEqual(new_code, _SCRIPT_SPLIT + code)

        code = ' src="js/test.js"></scrip>'
        new_code = _right_script(code, root_dir)
        self.assertEqual(new_code, _SCRIPT_SPLIT + code)

        code = ' src="js/test.js"></script> code'
        new_code = _right_script(code, root_dir)
        self.assertNotEqual(new_code, _SCRIPT_SPLIT + code)

        code = ' src="js/test.js"></script>'
        new_code = _right_script(code, root_dir)
        self.assertNotEqual(new_code, _SCRIPT_SPLIT + code)
