# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
from source.arguments import HELPERS
from source.parser.root_html import root_html_parser
from source.printers.help import show_help
from source.printers.wrong_arg import error_arguments


def call_function(option):
    """
        Call a function depending on the option
    :param option: the string option
    """

    if option in HELPERS:
        show_help()
        return

    if ".html" in option:
        root_html_parser(option)
        return

    error_arguments()
