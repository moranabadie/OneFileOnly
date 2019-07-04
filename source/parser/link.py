# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""
from source.img.get_img import get_image
from source.reader.get_content import get_content


def link_parser(original_code, link_code, src_possibility,
                folder, pattern, right_of_end_script):
    """
        Find the src inside the script
    :param right_of_end_script: whats on the right of the code to change
        :type right_of_end_script: str
    :param pattern: the linker structure
        :type pattern: CodePattern
    :param original_code: The original code
        :type original_code: str
    :param link_code: the code to parse with the link inside
        :type link_code: str
    :param src_possibility: one of the different way of writing src
        :type src_possibility: (str, str)
    :param folder: the folder of the html file
        :type folder: str
    :return: the replaced code
        :rtype: str
    """
    # 1. Get the url/link to the file
    (left, right) = src_possibility
    split_script = link_code.split(left)
    if len(split_script) < 2:
        return pattern.original + original_code
    left_of_split = split_script[0]
    right_of_src = split_script[1]
    split_script = right_of_src.split(right)
    if len(split_script) < 2:
        return pattern.original + original_code
    inside = split_script[0]
    # 2. Get the content of the file
    if pattern.is_img:
        # 2.1. Get the content of the image
        content = get_image(inside, folder)
        extra = ""
        for elem in split_script[1:]:
            extra += right + elem
        extra += pattern.end
    else:
        # 2.2. Get the content of the non binary file
        content = get_content(inside, folder)
        left_of_split = ""
        extra = pattern.between_right + pattern.end
    # 3. If nothing is found, return the original code
    if content is None:
        return pattern.original + original_code
    # 4. Return the changed code
    new_code = (pattern.full + left_of_split + pattern.between_left + content +
                extra)
    return new_code + right_of_end_script
