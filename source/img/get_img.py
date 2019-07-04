# coding=utf-8
"""
    Created by Abadie Moran at 03/07/2019

"""
from source.img.convert import path_to_bin
from source.internet.download import download_from_link


def get_image(path, folder):
    """
        Try to get the image of a file
    :param path: the path of the image file
    :param folder: the folder of the html file
    :return: the binary or None if it is not found
    """
    content = path_to_bin(path)
    if content is None:
        content = path_to_bin(folder + "/" + path)
    if content is None:
        content = download_from_link(path, is_img=True)
    return content
