# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""

WRONG_ARG_MESSAGE = "An error occurred : wrong number of arguments"
AN_ERROR = "Unable to read the arguments"


def print_wrong_argument():
    """
        When the users use a wrong number of arguments
    """
    print(WRONG_ARG_MESSAGE)


def error_arguments():
    """
        Print when an error occurred with the command arguments
    """
    print(AN_ERROR)
