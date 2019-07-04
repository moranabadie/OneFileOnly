# coding=utf-8
"""
    Created by Abadie Moran at 04/07/2019

"""


def get_file_type(path):
    """
        Get the type of a file
    :param path:  the path of the file
    :return: its type
    """
    format_split = path.split(".")
    format_file = format_split[len(format_split) - 1]
    format_file = format_file.lower()
    format_file = format_file.replace("jpg", "jpeg")
    return format_file
