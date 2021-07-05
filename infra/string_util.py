import re


def is_unique_str(txt):
    return re.match("[a-zA-Z0-9,\/@#$% ]+", txt)


# TODO: fix REGEX
def identifier_generator(project_name):
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
