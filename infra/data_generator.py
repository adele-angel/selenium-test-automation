import configparser
import string
import random


class DataGenerator:
    @staticmethod
    def random_str_generator(size=255, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for i in range(size))

    @staticmethod
    def identifier_generator(size=255, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for i in range(size))
