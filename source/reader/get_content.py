# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""
import warnings

from source.internet.download import download_from_link
from source.reader.file import file_to_str


def get_content(path, folder):
    """
        Try to get the content of the js file
    :param path: the path of the js file
    :param folder: the folder of the html file
    :return: the content of the file
    """
    content = file_to_str(path, False)
    if content is None:
        warnings.simplefilter("ignore")
        content = file_to_str(folder + "/" + path, False)
        warnings.simplefilter("default")
    if content is None:
        content = download_from_link(path)
    return content
