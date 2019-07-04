# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser.pattern import CodePattern
from source.parser.replace_pattern import replace_pattern


def replace_img(html_code, folder):
    """
        Put the image dependency into the new html file
    :param folder: the folder of the main html file
        :type folder: str
    :param html_code: the HTML code of the main html file
        :type html_code: str
    :return: the updated code
        :rtype: str

    Examples :

    # When it is well structured
    code = '<img src="img/file.jpg">'
    replace_img(code, "/home/path/")
    >> <img sr="data:image/jpeg;base64,/9j/4[...]fo">

    # When it is not well structured (wrong typo : sr)
    code = '<img sr="img/file.jpg">'
    replace_img(code, "/home/path/")
    >> <img sr="img/file.jpg">

    """
    return replace_pattern(html_code, folder, CodePattern(CodePattern.IMG))
