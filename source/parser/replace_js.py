# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser.pattern import CodePattern
from source.parser.replace_pattern import replace_pattern


def replace_js(html_code, folder):
    """
        Put the outside js file into the html file
    :param folder: the folder of the html file
    :param html_code: the HTML code
    :return: the updated code
    """
    return replace_pattern(html_code, folder, CodePattern(CodePattern.SCRIPT))
