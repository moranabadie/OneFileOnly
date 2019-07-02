# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
from source.parser.replace_css import replace_css
from source.parser.replace_js import replace_js
from source.reader.file import file_to_str
from source.reader.get_folder import get_folder_of_file


def root_html_parser(path):
    """
        Parse the user root HTML, to find dependencies and replace them
    :param path: the path of the main html
    """
    content = file_to_str(path)
    folder = get_folder_of_file(path)
    new_code = replace_js(content, folder)
    new_code = replace_css(new_code, folder)
    return new_code
