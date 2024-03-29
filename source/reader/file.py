# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
import mimetypes
import sys


def file_to_str(file_path, exit_when_fails=True):
    """
        Get the string content of a file
=
    :param exit_when_fails: exit when the call fails
        :type exit_when_fails: bool
    :param file_path: the file path
        :type file_path: str
    :return: the content of the file
        :rtype: str
    """
    (type_file, _) = mimetypes.guess_type(file_path)
    if "image" in str(type_file):
        return None

    if sys.version_info[0] < 3:  # pragma: no cover
        error_concept = IOError
    else:
        error_concept = FileNotFoundError

    try:
        file = open(file_path)
        content = file.read()
        file.close()
    except (UnicodeDecodeError, error_concept) as _:
        if exit_when_fails:
            print("Error : No such file : " + file_path)
            sys.exit(1)
        else:
            return None
    return content


def str_to_file(file_path, content):
    """
        Write a string into a file

    :param content: the content of the new file
        :type content: str
    :param file_path: the file path
        :type file_path: str
    """
    try:
        f = open(file_path, "w")
        try:
            f.write(content)
        finally:
            f.close()
    except IOError:
        print("Error : Cannot write into a file : " + file_path)
        sys.exit(1)
