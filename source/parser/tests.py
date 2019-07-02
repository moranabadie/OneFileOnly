"""
    Testing the folder
"""
import os
import unittest

from source import ROOT_DIR
from source.parser.replace_js import _right_script, _src_parser, _SCRIPT_SPLIT, _SCRIPT_END_SPLIT, \
    replace_js
from source.parser.root_html import root_html_parser
from source.reader.get_content import get_content


class MyTestCase(unittest.TestCase):

    def test_root_html(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        new_code = root_html_parser(path_root)
        content_js_1 = get_content(root_dir + '/js/test.js', "")
        content_js_2 = get_content(root_dir + '/js/test2.js', "")
        self.assertTrue(content_js_1 in new_code)
        self.assertTrue(content_js_2 in new_code)

        self.assertTrue(root_dir + '/js/test.js' not in new_code)
        self.assertTrue(root_dir + '/js/test2.js' not in new_code)

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

        content = get_content(root_dir + '/js/test.js', "")
        code = ' src="js/test.js">'
        new_code = _src_parser(code + _SCRIPT_END_SPLIT, code, ('src="', '"'), root_dir)
        self.assertEqual(new_code, "<script>\n" + content + "\n</script>")

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

        content_js_1 = get_content(root_dir + '/js/test.js', "")
        self.assertEqual(new_code, "<script>\n" + content_js_1 + "\n</script>")

        code = '<script src="' + root_dir + '/js/test.js"></script>test'
        new_code = replace_js(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_js_1 = get_content(root_dir + '/js/test.js', "")
        self.assertEqual(new_code, "<script>\n" + content_js_1 + "\n</script>test")

        code = 'test<script src="' + root_dir + '/js/test.js"></script>test'
        new_code = replace_js(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_js_1 = get_content(root_dir + '/js/test.js', "")
        content_js_2 = get_content(root_dir + '/js/test2.js', "")
        self.assertEqual(new_code, "test<script>\n" + content_js_1 + "\n</script>test")

        code = get_content(root_dir + '/test.html', "")
        new_code = replace_js(code, root_dir)
        self.assertNotEqual(new_code, code)
        split = code.split("\n")
        self.assertTrue(content_js_1 in new_code)
        self.assertTrue(content_js_2 in new_code)
        self.assertTrue(split[0] in new_code)
        self.assertTrue(split[len(split) - 1] in new_code)
