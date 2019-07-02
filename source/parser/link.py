# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""
from source.parser import _SCRIPT_SPLIT_FULL, _SCRIPT_SPLIT, _SCRIPT_END_SPLIT
from source.reader.get_content import get_content


def link_parser(original_code, link_code, src_possibility, folder):
    """
        Find the src inside the script
    :param original_code: The original code
    :param link_code: the code to parse with the link inside
    :param src_possibility: one of the different way of writing src
    :param folder: the folder of the html file
    :return: the replaced code
    """
    (left, right) = src_possibility
    split_script = link_code.split(left)
    if len(split_script) < 2:
        return _SCRIPT_SPLIT + original_code
    right_of_src = split_script[1]
    split_script = right_of_src.split(right)
    if len(split_script) < 2:
        return _SCRIPT_SPLIT + original_code
    inside = split_script[0]
    content = get_content(inside, folder)
    if content is None:
        return _SCRIPT_SPLIT + original_code
    new_code = _SCRIPT_SPLIT_FULL + "\n" + content + "\n" + _SCRIPT_END_SPLIT
    return new_code
