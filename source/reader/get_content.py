# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""
from source.reader.file import file_to_str


def get_content(path, folder):
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
