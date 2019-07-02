# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser import _SCRIPT_SPLIT
from source.parser.inside import inside_parse


def replace_js(html_code, folder):
    """
        Put the outside js file into the html file
    :param folder: the folder of the html file
    :param html_code: the HTML code
    :return: the updated code
    """
    # 1. Split <script
    split_script = html_code.split(_SCRIPT_SPLIT)
    if len(split_script) < 2:
        return html_code
    # 2. Add the code on the left of the first <script
    new_code = split_script[0]
    # 3. Try to replace every scripts
    for split in split_script[1:]:
        new_code += inside_parse(split, folder)
    return new_code


