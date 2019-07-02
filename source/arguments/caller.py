# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
from source import ROOT_DIR
from source.arguments import HELPERS
from source.parser.root_html import root_html_parser
from source.printers.help import show_help
from source.printers.wrong_arg import error_arguments
from source.reader.file import str_to_file


def call_function(options):
    """
        Call a function depending on the option
    :param options: the string option
    """
    first_option = options[0]
    if first_option in HELPERS:
        show_help()
        return

    if ".html" in first_option:
        new_code = root_html_parser(first_option)
        if len(options) < 2:
            basic_path = ROOT_DIR + "/../one_file.html"
        else:
            basic_path = options[1]
        str_to_file(basic_path, new_code)
        return

    error_arguments()
