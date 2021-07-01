import string
import random
import re


class DataGenerator:

    def random_str_generator(size=255, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for i in range(size))

    def identifier_generator(project_name):
        identifier = re.sub('[^a-zA-Z0-9-]+', '-', project_name)
        if identifier[-1] == "-":
            identifier = identifier[:-1]
        return identifier.lower()
