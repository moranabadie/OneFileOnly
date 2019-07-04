# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""
import warnings

from source.internet.download import download_from_link
from source.reader.file import file_to_str


def get_content(path, folder):
    """
        Try to get the content of a file in a string
        without knowing if it is an url or a file.
    :param path: the path of the file
        :type path: str
    :param folder: the folder of the main html file
        :type folder: str
    :return: the content of the file
        :rtype: Union[None, str]

    Examples:

    # Use a local path relative to the main html file
    get_content("css/file.css", "/home/path/")
    >> "h1 {\nwidth: 50px;\n}\n"

    # Use a global path
    get_content("/home/path/css/file.css", "/home/path/")
    >> "h1 {\nwidth: 50px;\n}\n"

    # Use an url
    get_content("https://url.com/file.css", "/home/path/")
    >> "h1 {\nwidth: 50px;\n}\n"

    """
    content = file_to_str(path, False)
    if content is None:
        warnings.simplefilter("ignore")
        content = file_to_str(folder + "/" + path, False)
        warnings.simplefilter("default")
    if content is None:
        content = download_from_link(path)
    return content
