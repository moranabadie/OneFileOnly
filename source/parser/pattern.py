# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""

_SCRIPT_SPLIT_NO_SPACE = "<script"
_SCRIPT_SPLIT_FULL = _SCRIPT_SPLIT_NO_SPACE + ">"
_SCRIPT_SPLIT = _SCRIPT_SPLIT_NO_SPACE + " "
_SCRIPT_END_SPLIT = "</script>"
_SRC_POSSIBILITIES = [("src='", "'"), ('src="', '"')]

_CSS_ORIGINAL_NO_SPACE = "<link"
_CSS_END_NO_SPACE = "<style>"
_CSS_SPLIT_FULL = _CSS_END_NO_SPACE + ">"
_CSS_SPLIT = _CSS_ORIGINAL_NO_SPACE + " "
_CSS_ORIGINAL_END_SPLIT = ">"
_CSS_END_SPLIT = "</style>"
_HREF_POSSIBILITIES = [("href='", "'"), ('href="', '"')]


class CodePattern:
    """
        A code structure for scripts and css
    """

    def __init__(self, is_script):
        if is_script:
            self.full = _SCRIPT_SPLIT_FULL
            self.original = _SCRIPT_SPLIT
            self.original_end = _SCRIPT_END_SPLIT
            self.end = _SCRIPT_END_SPLIT
            self.possibilities = _SRC_POSSIBILITIES
        else:
            self.full = _CSS_END_NO_SPACE
            self.original = _CSS_SPLIT
            self.original_end = _CSS_ORIGINAL_END_SPLIT
            self.end = _CSS_END_SPLIT
            self.possibilities = _HREF_POSSIBILITIES