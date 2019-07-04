# coding=utf-8
"""
    Created by Abadie Moran at 28/06/2019

"""
from source.parser.inside import inside_parse


def replace_pattern(html_code, folder, pattern):
    """
        Remove external dependencies of the img/css/js code
    :param pattern: the pattern code for the css or the js
    :type pattern: CodePattern
    :param html_code: the html code to change
    :type html_code: str
    :param folder: the folder of the html file
    :type folder: str
    :return: the updated code
    :rtype: str

    Examples :

    # css
    pattern = CodePattern(CodePattern.CSS)
    code = '<script href="js/test.js" rel="stylesheet"></script>'
    replace_pattern(code, "/home/path"/, pattern)
    >> <script>var a = 0;</script>

    # js
    pattern = CodePattern(CodePattern.SCRIPT)
    code = '<script src="js/test.js"></script>'
    replace_pattern(code, "/home/path/", pattern)
    >> <script>var a = 0;</script>

    # img
    pattern = CodePattern(CodePattern.IMG)
    code = '<img src="img/file.jpg">'
    replace_pattern(code, "/home/path/", patter,)
    >> <img sr="data:image/jpeg;base64,/9j/4[...]fo">

    """
    # 1. Split <script
    split_script = html_code.split(pattern.original)
    if len(split_script) < 2:
        return html_code
    # 2. Add the code on the left of the first <script
    new_code = split_script[0]
    # 3. Try to replace every scripts
    for split in split_script[1:]:
        new_code += str(inside_parse(split, folder, pattern))
    return new_code
