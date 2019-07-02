# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser import _SCRIPT_SPLIT, _SCRIPT_END_SPLIT, _SRC_POSSIBILITIES
from source.parser.link import link_parser


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
        new_code += _right_script(split, folder)
    return new_code


def _right_script(split_code, folder):
    """
        Manage whats at the right of <script
    :param split_code: the split code at the right of each <script
    :param folder: the folder of the html file
    :return: the updated code
    """
    # 1. Split with the </script>
    split_script = split_code.split(_SCRIPT_END_SPLIT)
    # 2. If </script> is not found, return the original script code
    if len(split_script) < 2:
        return _SCRIPT_SPLIT + split_code
    # 3. Get the code inside <script and </script>
    inside = split_script[0]
    # 4. For each src possibilities
    for possibility in _SRC_POSSIBILITIES:
        (left, _) = possibility
        # 4.1 if the src is in the code, its the right one
        if left in inside:
            # 4.2 Try to replace the code
            right_of_end_script = ""
            for extra_code in split_script[1:]:
                right_of_end_script += extra_code
            return link_parser(split_code, inside, possibility, folder) + right_of_end_script
    # 5. if nothing is found, return the original script
    return _SCRIPT_SPLIT + split_code
