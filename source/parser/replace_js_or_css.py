# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser.inside import inside_parse


def replace_css_or_js(html_code, folder, pattern):
    """
        Replace the js code or the css code
    :param pattern: the pattern code for the css or the js
    :param folder: the folder of the html file
    :param html_code: the HTML code
    :return: the updated code
    """
    # 1. Split <script
    split_script = html_code.split(pattern.original)
    if len(split_script) < 2:
        return html_code
    # 2. Add the code on the left of the first <script
    new_code = split_script[0]
    # 3. Try to replace every scripts
    for split in split_script[1:]:
        new_code += inside_parse(split, folder, pattern)
    return new_code
