# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
import sys

from source.printers.help import show_help
from source.printers.wrong_arg import print_wrong_argument

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_wrong_argument()
        show_help()
        sys.exit(1)
    option = sys.argv[1]
    print(option)
