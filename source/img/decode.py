# coding=utf-8
"""
    Created by Abadie Moran at 04/07/2019

"""
import base64
import sys

_BASE_64 = ";base64,"
_DATA_IMG = "data:image/"


def decode_img(image_read, format_file):
    """
        Decode an image in base64

    :param format_file: the format of the file
    :type format_file: str
    :param image_read: the image to read
    :type image_read: bytes
    :return: the decoded image
    :rtype: str

    Example:

    decode_img("/home/path/file.jpg", "jpeg")
    >> "data:image/jpeg;base64,/9j/4[...]gf"


    """
    if sys.version_info[0] < 3:  # pragma: no cover
        bytes_value = base64.b64encode(image_read)
    else:
        bytes_value = base64.encodebytes(image_read)
    plus = _DATA_IMG + format_file + _BASE_64
    return plus + bytes_value.decode("utf-8").replace("\n", "")
