# coding=utf-8
"""
    Created by Abadie Moran at 03/07/2019

"""
from source.img.convert import path_to_bin
from source.internet.download import download_from_link


def get_image(path, folder):
    """
        Try to get the image base 64 bytes of a file in a string
        without knowing if it is an url or a file.

    :param path: the path of the image file
    :type path: str
    :param folder: the folder of the main html file
    :type folder: str
    :return: the binary or None if it is not found
    :rtype: str

    Examples:

    # Use a local path relative to the main html file
    decode_img("img/file.jpg", "/home/path/")
    >> "data:image/jpeg;base64,/9j/4[...]gf"

    # Use a global path
    decode_img("/home/path/img/file.jpg", "/home/path/")
    >> "data:image/jpeg;base64,/9j/4[...]gf"

    # Use an url
    decode_img("https://url.com/file.jpg", "/home/path/")
    >> "data:image/jpeg;base64,/9j/4[...]gf"

    """
    content = path_to_bin(path)
    if content is None:
        content = path_to_bin(folder + "/" + path)
    if content is None:
        content = download_from_link(path, is_img=True)
    return content
