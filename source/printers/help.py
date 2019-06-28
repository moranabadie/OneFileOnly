# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
from source.arguments import HELPERS

SHOW_MESSAGE = "   ->  Show this message for help"


def show_help():
    """
        Show the help message
    """
    print("")
    print(HELPERS[0] + " " + HELPERS[1] + SHOW_MESSAGE)
    print("                     Ex: python run.py -h")
    print("file        ->  The root file")
    print("                     Ex: python run.py ./folder/file.html")
    print("")
