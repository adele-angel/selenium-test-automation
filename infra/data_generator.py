import string
import random
import re


class DataGenerator:

    def random_str_generator(size=255, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for i in range(size))

    # TODO: fix REGEX
    def identifier_generator(project_name):
        identifier=project_name.lower()
        identifier.replace("$", "dollars")
        identifier.replace("#", "number")
        identifier.replace("/", "number")
        identifier.replace("%", "number")
        # identifier = re.sub('[^a-z0-9-]+', '-', project_name)
        # if identifier[-1] == "-":
        #     identifier = identifier[:-1]
        return identifier
