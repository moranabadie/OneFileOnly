# coding=utf-8
"""
    Created by Abadie Moran at 02/07/2019

"""
from source.parser.link import link_parser


def inside_parse(split_code, folder, pattern):
    """
        Manage whats at the right of the <script/<link/<img

    :param pattern: the pattern code for the css or the js
    :type pattern: CodePattern
    :param split_code: the split code at the right of each <script
    :type split_code: str
    :param folder: the folder of the html file
    :type folder: str
    :return: the updated code
    :rtype: str

    Examples:

    # When it is not well constructed
    code = ' hre="css/test.css"'
    pattern = CodePattern(CodePattern.CSS)
    inside_parse(code, "/home/path/, pattern)
    >> <link href="css/test.css"

    # When it is well constructed
    code = ' href="css/test.css">'
    pattern = CodePattern(CodePattern.CSS)
    inside_parse(code, "/home/path/, pattern)
    >> <style>\nh1 {\nwidth: 50px;\n}\n</style>


    """
    # 1. Split with the </script>
    split_script = split_code.split(pattern.original_end)
    # 2. If </script> is not found, return the original script code
    if len(split_script) < 2:
        return pattern.original + split_code
    # 3. Get the code inside <script and </script>
    inside = split_script[0]
    # 4. For each src possibilities
    for possibility in pattern.possibilities:
        (left, _) = possibility
        # 4.1 if the src is in the code, its the right one
        if left in inside:
            # 4.2 Try to replace the code
            right_of_end_script = ""
            first = True
            for extra_code in split_script[1:]:
                plus_str = ""
                if not first:
                    plus_str = pattern.original_end
                first = False
                right_of_end_script += plus_str + extra_code
            new_code = link_parser(split_code, inside, possibility, folder,
                                   pattern, right_of_end_script)
            return new_code
    # 5. if nothing is found, return the original script
    return pattern.original + split_code
