# coding=utf-8
"""
    Created by Abadie Moran at 04/07/2019

"""
import sys

from source.img.decode import decode_img
from source.reader.file_type import get_file_type


def download_from_link(url, is_img=False):
    """
        Try to download a file from a file
    :param is_img: is the file an image ?
    :param url: the link of a file
    :return: the content of the file to download
    """
    if sys.version_info[0] < 3:  # pragma: no cover
        # noinspection PyUnresolvedReferences
        import urllib2
        try:
            response = urllib2.urlopen(url)
        except (ValueError, urllib2.URLError) as _:
            return None
    else:
        import urllib.request
        # noinspection PyUnresolvedReferences
        try:
            response = urllib.request.urlopen(url)
        except (urllib.error.URLError, ValueError) as _:
            return None
    if is_img:
        format_file = get_file_type(url)
        return decode_img(response.read(), format_file)
    else:
        return response.read().decode("utf-8")
