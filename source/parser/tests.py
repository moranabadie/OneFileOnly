# coding=utf-8
"""
    Testing the folder
"""
import os
import unittest

from source import ROOT_DIR
from source.img.get_img import get_image
from source.parser.inside import inside_parse
from source.parser.link import link_parser
from source.parser.pattern import _SCRIPT_SPLIT, CodePattern, \
    _CSS_ORIGINAL_END_SPLIT, _CSS_SPLIT, _IMG_SPLIT
from source.parser.replace_css import replace_css
from source.parser.replace_img import replace_img
from source.parser.replace_js import replace_js
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
        for pat in [CodePattern.SCRIPT, CodePattern.IMG]:
            pattern = CodePattern(pat)
            code = ' src=js/test.js>'
            new_code = link_parser(code + pattern.original_end, code,
                                   ('src="', '"'), root_dir, pattern, "")
            self.assertEqual(new_code, pattern.original + code +
                             pattern.original_end)
            code = ' src="js/test.js\'>'
            new_code = link_parser(code + pattern.original_end, code,
                                   ('src="', '"'), root_dir, pattern, "")
            self.assertEqual(new_code, pattern.original + code +
                             pattern.original_end)

            code = ' src="js/test.js">'
            new_code = link_parser(code + pattern.original_end, code,
                                   ('src="', '"'), root_dir, pattern, "")
            self.assertNotEqual(new_code, pattern.original + code +
                                pattern.original_end)

            code = ' src="js/test.j">'
            new_code = link_parser(code + pattern.original_end, code,
                                   ('src="', '"'), root_dir, pattern, "")
            self.assertEqual(new_code, pattern.original + code +
                             pattern.original_end)

            if pat == CodePattern.IMG:
                code = 'src="img/tiny.png"'
                content = get_content(root_dir + '/img/png.txt', "")

            else:
                code = ' src="js/test.js">'
                content = get_content(root_dir + '/js/test.js', "")

            new_code = link_parser(code + pattern.original_end, code,
                                   ('src="', '"'), root_dir, pattern, "")
            if pat == CodePattern.SCRIPT:
                self.assertEqual(new_code, "<script>\n" + content + "\n</script>")
            else:
                self.assertEqual(new_code, "<img src=\"" + content + "\">")

            if pat == CodePattern.IMG:
                code = 'alt="test" src="img/tiny.png"'
                content = get_content(root_dir + '/img/png.txt', "")

                new_code = link_parser(code + pattern.original_end, code,
                                       ('src="', '"'), root_dir, pattern, "")

                self.assertEqual(new_code, '<img alt="test" src=\"' + content + "\">")

                code = 'alt="test" src="img/tiny.png" width="2" /'
                content = get_content(root_dir + '/img/png.txt', "")

                new_code = link_parser(code + pattern.original_end, code,
                                       ('src="', '"'), root_dir, pattern, "")

                self.assertEqual(new_code, '<img alt="test" src=\"' + content + '\" width="2" />')

                code = 'src="img/tiny.png" width="2" alt="test"/'
                content = get_content(root_dir + '/img/png.txt', "")

                new_code = link_parser(code + pattern.original_end, code,
                                       ('src="', '"'), root_dir, pattern, "")

                self.assertEqual(new_code, '<img src=\"' + content + '\" width="2" alt="test"/>')

    def test_replace_href(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        pattern = CodePattern(CodePattern.CSS)
        code = ' href=js/test.js'
        new_code = link_parser(code + _CSS_ORIGINAL_END_SPLIT, code,
                               ('href="', '"'), root_dir, pattern, "")
        self.assertEqual(new_code, _CSS_SPLIT + code +
                         _CSS_ORIGINAL_END_SPLIT)
        code = ' href="js/test.js\'>'
        new_code = link_parser(code + _CSS_ORIGINAL_END_SPLIT, code,
                               ('href="', '"'), root_dir, pattern, "")
        self.assertEqual(new_code, _CSS_SPLIT + code + _CSS_ORIGINAL_END_SPLIT)

        code = ' href="js/test.js">'
        new_code = link_parser(code + _CSS_ORIGINAL_END_SPLIT, code,
                               ('href="', '"'), root_dir, pattern, "")
        self.assertNotEqual(new_code, _CSS_SPLIT + code + _CSS_ORIGINAL_END_SPLIT)

        code = ' href="js/test.j">'
        new_code = link_parser(code + _CSS_ORIGINAL_END_SPLIT, code,
                               ('href="', '"'), root_dir, pattern, "")
        self.assertEqual(new_code, _CSS_SPLIT + code + _CSS_ORIGINAL_END_SPLIT)

        content = get_content(root_dir + '/css/test.css', "")
        code = ' href="css/test.css">'
        new_code = link_parser(code + _CSS_ORIGINAL_END_SPLIT, code,
                               ('href="', '"'), root_dir, pattern, "")
        self.assertEqual(new_code, "<style>\n" + content + "\n</style>")

    def test_inside_js(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        pattern = CodePattern(CodePattern.SCRIPT)
        code = ' src="js/test.js"></scrip>'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertEqual(new_code, _SCRIPT_SPLIT + code)

        code = ' src="js/test.js"></script> code'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertNotEqual(new_code, _SCRIPT_SPLIT + code)

        code = ' src="js/test.js"></script>'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertNotEqual(new_code, _SCRIPT_SPLIT + code)

    def test_inside_css(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        pattern = CodePattern(CodePattern.CSS)
        code = ' href="css/test.css"'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertEqual(new_code, _CSS_SPLIT + code)

        code = ' href="css/test.css"> code'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertNotEqual(new_code, _CSS_SPLIT + code)

        code = ' href="css/test.css"/> code'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertNotEqual(new_code, _CSS_SPLIT + code)

        code = ' href="css/test.css">'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertNotEqual(new_code, _CSS_SPLIT + code)

    def test_inside_img(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )
        pattern = CodePattern(CodePattern.IMG)
        code = ' src="img/tiny.png"'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertEqual(new_code, _IMG_SPLIT + code)

        code = ' src="img/tiny.png"> code'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertNotEqual(new_code, _IMG_SPLIT + code)

        code = ' src="img/tiny.png"/> code'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertNotEqual(new_code, _IMG_SPLIT + code)

        code = ' src="img/tiny.png">'
        new_code = inside_parse(code, root_dir, pattern)
        self.assertNotEqual(new_code, _IMG_SPLIT + code)

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

        code = '<script><script src="' + root_dir + '/js/test.js"></script>'
        new_code = replace_js(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_js_1 = get_content(root_dir + '/js/test.js', "")
        self.assertEqual(new_code, "<script><script>\n" + content_js_1 + "\n</script>")

        code = '<script src="' + root_dir + '/js/test.js"></script></script>'
        new_code = replace_js(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_js_1 = get_content(root_dir + '/js/test.js', "")
        self.assertEqual(new_code, "<script>\n" + content_js_1 + "\n</script></script>")

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

    def test_replace_css(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )

        code = '<lin href="css/test.css">'
        new_code = replace_css(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<link href="css/test.css"'
        new_code = replace_css(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<link href=css/test.css">'
        new_code = replace_css(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<link href=\'css/test.css">'
        new_code = replace_css(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<link href=\'js/test.j">'
        new_code = replace_css(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<link href="css/test.css">'
        new_code = replace_css(code, root_dir)
        self.assertNotEqual(new_code, code)

        code = '<link href="' + root_dir + '/css/test.css">'
        new_code = replace_css(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_css_1 = get_content(root_dir + '/css/test.css', "")
        self.assertEqual(new_code, "<style>\n" + content_css_1 + "\n</style>")

        code = '<link href="' + root_dir + '/css/test.css">test'
        new_code = replace_css(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_css_1 = get_content(root_dir + '/css/test.css', "")
        self.assertEqual(new_code, "<style>\n" + content_css_1 + "\n</style>test")

        code = 'test<link href="' + root_dir + '/css/test.css" />test'
        new_code = replace_css(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_css_1 = get_content(root_dir + '/css/test.css', "")
        self.assertEqual(new_code, "test<style>\n" + content_css_1 + "\n</style>test")

        code = 'test<link href="' + root_dir + \
               '/css/test.css" /><link rel="icon" href="img/favicon.ico" />'
        new_code = replace_css(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_css_1 = get_content(root_dir + '/css/test.css', "")
        self.assertEqual(new_code, "test<style>\n" + content_css_1 +
                         '\n</style><link rel="icon" href="img/favicon.ico" />')

        code = 'test<link rel="icon" href="img/favicon.ico" />test<link href="' + root_dir + \
               '/css/test.css" />test<link rel="icon" href="img/tiny.ico" />test'
        new_code = replace_css(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_css_1 = get_content(root_dir + '/css/test.css', "")
        content_css_2 = get_content(root_dir + '/css/test2.css', "")
        self.assertEqual(new_code,
                         'test<link rel="icon" href="img/favicon.ico" />test<style>\n' +
                         content_css_1 +
                         '\n</style>test<link rel="icon" href="img/tiny.ico" />test')

        code = get_content(root_dir + '/test.html', "")
        new_code = replace_css(code, root_dir)
        self.assertNotEqual(new_code, code)
        split = code.split("\n")
        self.assertTrue(content_css_1 in new_code)
        self.assertTrue(content_css_2 in new_code)
        self.assertTrue(split[0] in new_code)
        self.assertTrue(split[len(split) - 1] in new_code)

    def test_replace_img(self):
        path_root = ROOT_DIR + "/html_tests/test.html"
        root_dir = os.path.dirname(
            path_root
        )

        code = '<im src="img/tiny.png">'
        new_code = replace_img(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<img src="img/tiny.png"'
        new_code = replace_img(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<img src=img/tiny.png">'
        new_code = replace_img(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<img src=\'img/tiny.png">'
        new_code = replace_img(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<img src=\'img/tiny.pn">'
        new_code = replace_img(code, root_dir)
        self.assertEqual(new_code, code)

        code = '<img src="img/tiny.png">'
        new_code = replace_img(code, root_dir)
        self.assertNotEqual(new_code, code)

        code = '<img src="' + root_dir + '/img/tiny.png">'
        new_code = replace_img(code, root_dir)
        self.assertNotEqual(new_code, code)

        content_img_1 = get_image(root_dir + '/img/tiny.png', "")
        self.assertEqual(new_code, "<img src=\"" + content_img_1 + "\">")

        code = '<img src="' + root_dir + '/img/tiny.png">test'
        new_code = replace_img(code, root_dir)
        self.assertNotEqual(new_code, code)

        self.assertEqual(new_code, "<img src=\"" + content_img_1 + "\">test")

        code = 'test<img src="' + root_dir + '/img/tiny.png" />test'
        new_code = replace_img(code, root_dir)
        self.assertNotEqual(new_code, code)

        self.assertEqual(new_code, "test<img src=\"" + content_img_1 + "\" />test")

        code = 'test<img src="' + root_dir + \
               '/img/tiny.png" /><link rel="icon" href="img/favicon.ico" />'
        new_code = replace_img(code, root_dir)
        self.assertNotEqual(new_code, code)

        self.assertEqual(new_code, "test<img src=\"" + content_img_1 +
                         '\" /><link rel="icon" href="img/favicon.ico" />')

        code = 'test<link rel="icon" href="img/favicon.ico" />test<img src="' + root_dir + \
               '/img/tiny.png" />test<link rel="icon" href="img/tiny.ico" />test'
        new_code = replace_img(code, root_dir)
        self.assertNotEqual(new_code, code)