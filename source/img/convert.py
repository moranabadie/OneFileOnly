# coding=utf-8
"""
    Created by Abadie Moran at 03/07/2019

"""

from source.img.decode import decode_img
from source.reader.file_type import get_file_type


def path_to_bin(path):
    """
        Convert an image to a binary 64 string
    :type path: str
    :param path: the path of the image
    :return: the image binary or None if the file does not exists
    :rtype: Union[None, str]

    Examples :

    path_to_bin("/html_tests/img/file_which_does_not_exists.bmp")
    >> None

    path_to_bin("/html_tests/img/file_which_exists.bmp")
    >> "data:image/jpeg;base64,Qk2KA[...]k2KA"


    """
    format_file = get_file_type(path)
    if format_file == "" or len(format_file) > 4:
        return None
    try:
        image = open(path, 'rb')
        try:
            image_read = image.read()
            image_64_encode = decode_img(image_read, format_file)
            return image_64_encode
        finally:
            image.close()
    except IOError:
        pass
    return None
