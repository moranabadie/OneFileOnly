# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""
from source.reader.get_content import get_content


def link_parser(original_code, link_code, src_possibility,
                folder, pattern, right_of_end_script):
    """
        Find the src inside the script
    :param right_of_end_script: whats on the right of the code to change
    :param pattern: the linker structure
    :param original_code: The original code
    :param link_code: the code to parse with the link inside
    :param src_possibility: one of the different way of writing src
    :param folder: the folder of the html file
    :return: the replaced code
    """
    (left, right) = src_possibility
    split_script = link_code.split(left)
    if len(split_script) < 2:
        return pattern.original + original_code
    right_of_src = split_script[1]
    split_script = right_of_src.split(right)
    if len(split_script) < 2:
        return pattern.original + original_code
    inside = split_script[0]
    content = get_content(inside, folder)
    if content is None:
        return pattern.original + original_code
    new_code = pattern.full + "\n" + content + "\n" + pattern.end
    return new_code + right_of_end_script
