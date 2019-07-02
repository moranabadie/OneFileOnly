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
    print("file        ->  Convert the html file into another without dependencies")
    print("                     Ex: python run.py ./folder/file.html")
    print("file1 file2 ->  Convert file1 into another file named file2 without dependencies")
    print("                     Ex: python run.py ./folder/file.html ./folder/file2.html")
    print("")
