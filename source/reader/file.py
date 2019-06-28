# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
import sys


def file_to_str(file_path):
    """
        Get the string content of a file
    :param file_path: the file path
    :return:
    """
    try:
        file = open(file_path)
        content = file.read()
        file.close()
    except FileNotFoundError as _:
        print("Error : No such file : " + file_path)
        sys.exit(1)
    return content
