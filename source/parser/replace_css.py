# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser.pattern import CodePattern
from source.parser.replace_pattern import replace_pattern


def replace_css(html_code, folder):
    """
        Put the dependency css file into the new html file

    :param folder: the folder of the main html file
        :type folder: str
    :param html_code: the HTML code of the main html file
        :type html_code: str
    :return: the updated code
        :rtype: str

    Examples :

    # When it is well structured
    code = '<link href="css/test.css" rel="stylesheet">'
    replace_css(code, "/home/path/")
    >> <style>\nh1 {\nwidth: 50px;\n}\n</style>

    # When it is not well structured (wrong typo : hre)
    code = '<link hre="css/test.css" rel="stylesheet">'
    replace_css(code, "/home/path/")
    >> <link hre="css/test.css" rel="stylesheet">

    """
    return replace_pattern(html_code, folder, CodePattern(CodePattern.CSS))
