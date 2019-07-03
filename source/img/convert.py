# coding=utf-8
"""
    Created by Abadie Moran at 03/07/2019

"""
import base64

_BASE_64 = ";base64,"
_DATA_IMG = "data:image/"


def path_to_bin(path):
    """
        Convert an image to a binary 64
    :param path: the path of the image
    :return: the image binary or None if the file does not exists
    """
    format_split = path.split(".")
    format_file = format_split[len(format_split) - 1]
    format_file = format_file.lower()
    format_file = format_file.replace("jpg", "jpeg")
    if format_file == "" or len(format_file) > 4:
        return None
    try:
        image = open(path, 'rb')
        try:
            image_read = image.read()

            image_64_encode = (_DATA_IMG + format_file + _BASE_64
                               + base64.encodebytes(image_read).
                               decode("utf-8").replace("\n", ""))
            return image_64_encode
        finally:
            image.close()
    except IOError:
        pass
    return None
