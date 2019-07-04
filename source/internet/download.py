# coding=utf-8
"""
    Created by Abadie Moran at 04/07/2019

"""
import sys

from source.img.decode import decode_img
from source.reader.file_type import get_file_type


def download_from_link(url, is_img=False):
    """
        Try to download a file
    :param is_img: is a file or an image ?
    :type is_img: bool
    :param url: the url of a file
    :type url: str
    :return: the content of the file to download
    :rtype: str

    Examples:

    download_from_link("https://url.com/img/file.jpg", is_img=True)
    >> "data:image/jpeg;base64,/9j/4[...]gf"

    download_from_link("https://url.com/css/file.css", is_img=False)
    >> "h1 {\nfont-size:50px;\n}"

    """
    # 1. Load the content of the url
    if sys.version_info[0] < 3:  # pragma: no cover
        # 1.1. If it is python 2.x
        # noinspection PyUnresolvedReferences
        import urllib2
        try:
            response = urllib2.urlopen(url)
        except (ValueError, urllib2.URLError) as _:
            return None
    else:
        # 1.2. If it is python 3.x
        import urllib.request
        # noinspection PyUnresolvedReferences
        try:
            response = urllib.request.urlopen(url)
        except (urllib.error.URLError, ValueError) as _:
            return None
    # 2. Decode the content
    if is_img:
        format_file = get_file_type(url)
        return decode_img(response.read(), format_file)
    else:
        return response.read().decode("utf-8")
