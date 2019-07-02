# coding=utf-8
"""
    Created by Abadie Moran at 27/06/2019

"""
_SCRIPT_SPLIT_NO_SPACE = "<script"
_SCRIPT_SPLIT_FULL = _SCRIPT_SPLIT_NO_SPACE + ">"
_SCRIPT_SPLIT = _SCRIPT_SPLIT_NO_SPACE + " "
_SCRIPT_END_SPLIT = "</script>"
_SRC_POSSIBILITIES = [("src='", "'"), ('src="', '"')]
