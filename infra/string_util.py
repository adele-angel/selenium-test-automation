import re


def is_unique_str(txt):
    """
    Checks if given string is unique.
    A string is unique if it contains letters (upper & lower case), numbers, spaces and special characters.

    Args:
        txt (str): given project name or work package subject.

    Returns:
        bool: True if given string is unique, else False.
    """
    return re.match("[a-zA-Z0-9,\/@#$% ]+", txt)


# TODO: fix REGEX
def identifier_generator(project_name):
    """
    Generates an identifier from a given project name.
    The identifier matches the value entered for the project name, with all lowercase letters,
    and all the spaces and special characters replaced with a dash.

    Note:
        OpenProject's identifier field doesn't match project requirements for special characters.
        Using some special characters such as $, ^, \ etc. might result an invalid identifier.

    Args:
        project_name (str): given project name.

    Returns:
        str: generated identifier.
    """
    dct = {
        '#': 'number',
        '@': 'at',
        '&': 'and',
        '$': 'dollars',
        '%': 'percent',
        '/': 'slash',
        '.': 'dot'
    }
    identifier = re.sub(r"[$@#]", lambda x: f"-{dct[x.group()]}-", project_name)
    identifier = re.sub("[^a-zA-Z0-9@#$&]+", "-", " ".join(identifier.lower().split()))
    return identifier.strip('-')
