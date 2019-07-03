# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""

_IMG_SPLIT_NO_SPACE = "<img"
_IMG_SPLIT_FULL = _IMG_SPLIT_NO_SPACE + " "
_IMG_SPLIT = _IMG_SPLIT_NO_SPACE + " "
_IMG_ORIGINAL_END_SPLIT = ">"
_IMG_END_SPLIT = ">"

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
    SCRIPT = 0
    CSS = 1
    IMG = 2

    def __init__(self, pattern):
        self.is_img = pattern == self.IMG
        if pattern == self.SCRIPT:
            self.full = _SCRIPT_SPLIT_FULL
            self.original = _SCRIPT_SPLIT
            self.original_end = _SCRIPT_END_SPLIT
            self.end = _SCRIPT_END_SPLIT
            self.possibilities = _SRC_POSSIBILITIES
            self.between_right = "\n"
            self.between_left = "\n"
        elif self.is_img:
            self.full = _IMG_SPLIT_FULL
            self.original = _IMG_SPLIT
            self.original_end = _IMG_ORIGINAL_END_SPLIT
            self.end = _IMG_END_SPLIT
            self.possibilities = _SRC_POSSIBILITIES
            self.between_right = "\""
            self.between_left = "src=\""
        else:
            self.full = _CSS_END_NO_SPACE
            self.original = _CSS_SPLIT
            self.original_end = _CSS_ORIGINAL_END_SPLIT
            self.end = _CSS_END_SPLIT
            self.possibilities = _HREF_POSSIBILITIES
            self.between_right = "\n"
            self.between_left = "\n"
