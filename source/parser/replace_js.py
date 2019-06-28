# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.reader.file import file_to_str

_SCRIPT_SPLIT = "<script "
_SCRIPT_END_SPLIT = "</script>"
_SRC_POSSIBILITIES = [("src='", "'"), ('src="', '"')]


def replace_js(html_code, folder):
    """
        Put the outside js file into the html file
    :param folder: the folder of the html file
    :param html_code: the HTML code
    :return: the updated code
    """
    split_script = html_code.split(_SCRIPT_SPLIT)
    if len(split_script) < 1:
        return html_code
    new_code = split_script[0]
    for split in split_script[1:]:
        new_code += _right_script(split, folder)
    return new_code


def _right_script(split_code, folder):
    """
        Manage whats at the right of <script
    :param split_code: the split code at the right of each <script
    :param folder: the folder of the html file
    :return: the updated code
    """
    split_script = split_code.split(_SCRIPT_END_SPLIT)
    if len(split_script) < 2:
        return _SCRIPT_SPLIT + split_code
    inside = split_script[0]
    for possibility in _SRC_POSSIBILITIES:
        (left, _) = possibility
        if left in inside:
            return _src_parser(inside, possibility, folder)

    return _SCRIPT_SPLIT + split_code


def _src_parser(split_code, src_possibility, folder):
    """
        Find the src inside the script
    :param split_code: the code to parse
    :param src_possibility: one of the different way of writing src
    :param folder: the folder of the html file
    :return: the replaced code
    """
    (left, right) = src_possibility
    split_script = split_code.split(left)
    if len(split_script) < 2:
        return _SCRIPT_SPLIT + split_code
    right_of_src = split_script[1]
    split_script = right_of_src.split(right)
    if len(split_script) < 2:
        return _SCRIPT_SPLIT + split_code
    inside = split_script[0]
    content = _get_content(inside, folder)
    print(content)
    return inside


def _get_content(path, folder):
    """
        Try to get the content of the js file
    :param path: the path of the js file
    :param folder: the folder of the html file
    :return:
    """
    content = file_to_str(path, False)
    if content is None:
        content = file_to_str(folder + "/" + path, False)
    return content
