# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser.pattern import CodePattern
from source.parser.replace_js_or_css import replace_css_or_js


def replace_css(html_code, folder):
    """
        Put the outside css file into the html file
    :param folder: the folder of the html file
    :param html_code: the HTML code
    :return: the updated code
    """
    return replace_css_or_js(html_code, folder, CodePattern(False))
