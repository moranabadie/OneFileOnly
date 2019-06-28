# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
import os


def get_folder_of_file(file_path):
    """
        Get the folder of the file
    :param file_path: the file path
    :return: the folder path
    """
    return os.path.dirname(file_path)
