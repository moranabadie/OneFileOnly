# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
from source.reader.file import file_to_str


def root_html_parser(path):
    """
        Parse the user root HTML, to find dependencies and replace them
    :param path: the path of the main html
    """
    content = file_to_str(path)
