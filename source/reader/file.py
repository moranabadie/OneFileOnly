# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
import sys


def file_to_str(file_path, exit_when_fails=True):
    """
        Get the string content of a file
    :param exit_when_fails: exit when the call fails
    :param file_path: the file path
    :return:
    """
    try:
        file = open(file_path)
        content = file.read()
        file.close()
    except FileNotFoundError as _:
        if exit_when_fails:
            print("Error : No such file : " + file_path)
            sys.exit(1)
        else:
            return None
    return content
