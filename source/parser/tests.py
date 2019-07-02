"""
    Testing the folder
"""
import os
import unittest

from source import ROOT_DIR
from source.parser.replace_js import _right_script, _src_parser, _SCRIPT_SPLIT, _get_content, \
    _SCRIPT_END_SPLIT, replace_js


class MyTestCase(unittest.TestCase):
    def test_get_content(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        js_path = root_dir + "/js/test.j"
        content = _get_content(js_path, root_dir)
        self.assertEqual(content, None)
        js_path = root_dir + "/js/test.js"
        content = _get_content(js_path, root_dir)
        self.assertNotEqual(content, None)
        js_path = "js/test.j"
        content = _get_content(js_path, root_dir)
        self.assertEqual(content, None)

        js_path = "js/test.js"
        content = _get_content(js_path, root_dir)
        self.assertNotEqual(content, None)

    def test_replace_src(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        code = ' src=js/test.js>'
        new_code = _src_parser(code + _SCRIPT_END_SPLIT, code, ('src="', '"'), root_dir)
        self.assertEqual(new_code, _SCRIPT_SPLIT + code + _SCRIPT_END_SPLIT)
        code = ' src="js/test.js\'>'
        new_code = _src_parser(code + _SCRIPT_END_SPLIT, code, ('src="', '"'), root_dir)
        self.assertEqual(new_code, _SCRIPT_SPLIT + code + _SCRIPT_END_SPLIT)

        code = ' src="js/test.js">'
        new_code = _src_parser(code + _SCRIPT_END_SPLIT, code, ('src="', '"'), root_dir)
        self.assertNotEqual(new_code, _SCRIPT_SPLIT + code + _SCRIPT_END_SPLIT)

        code = ' src="js/test.j">'
        new_code = _src_parser(code + _SCRIPT_END_SPLIT, code, ('src="', '"'), root_dir)
        self.assertEqual(new_code, _SCRIPT_SPLIT + code + _SCRIPT_END_SPLIT)

    def test_replace_right(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        code = ' src="js/test.js"></scrip>'
        new_code = _right_script(code, root_dir)
        self.assertEqual(new_code, _SCRIPT_SPLIT + code)

        code = ' src="js/test.js"></script> code'
        new_code = _right_script(code, root_dir)
        self.assertNotEqual(new_code, _SCRIPT_SPLIT + code)

        code = ' src="js/test.js"></script>'
        new_code = _right_script(code, root_dir)
        self.assertNotEqual(new_code, _SCRIPT_SPLIT + code)

    def test_replace_js(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )

        code = '<scrip src="js/test.js"></script>'
        new_code = replace_js(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<script src="js/test.js"></script'
        new_code = replace_js(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<script src=js/test.js"></script>'
        new_code = replace_js(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<script src=\'js/test.js"></script>'
        new_code = replace_js(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<script src=\'js/test.j"></script>'
        new_code = replace_js(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<script src="js/test.js"></script>'
        new_code = replace_js(code, root_dir)
        self.assertNotEqual(new_code, code)

        code = '<script src="' + root_dir + '/js/test.js"></script>'
        new_code = replace_js(code, root_dir)
        self.assertNotEqual(new_code, code)

        content = _get_content(root_dir + '/js/test.js', "")
        self.assertEqual(new_code, "<script>\n" + content + "\n</script>")
