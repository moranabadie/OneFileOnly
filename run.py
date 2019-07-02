# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
import sys

from source.arguments.caller import call_function
from source.printers.help import show_help
from source.printers.wrong_arg import print_wrong_argument

if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) not in [2, 3]:
        print_wrong_argument()
        show_help()
        sys.exit(1)
    options = sys.argv[1:]
    call_function(options)
