# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser.pattern import CodePattern
from source.parser.replace_pattern import replace_pattern


def replace_js(html_code, folder):
    """
        Put the dependency js file into the new html file

    :param folder: the folder of the main html file
        :type folder: str
    :param html_code: the HTML code of the main html file
        :type html_code: str
    :return: the updated code
        :rtype: str

    Examples :

    # When it is well structured
    code = '<script src="js/test.js"></script>'
    replace_js(code, "/home/path/")
    >> <script>var a = 0;</script>

    # When it is not well structured (wrong typo : sr)
    code = '<script sr="js/test.js"></script>'
    replace_js(code, "/home/path/")
    >> <script sr="js/test.js" rel="stylesheet"></script>
    """
    return replace_pattern(html_code, folder, CodePattern(CodePattern.SCRIPT))
