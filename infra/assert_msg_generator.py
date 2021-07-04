class AssertMsgGenerator:
    def __init__(self, action, obj, attr):
        self.action = action
        self.obj = obj
        self.attr = attr

    def create_msg(self, actual):
        return f'Failed to get {self.action} {self.obj} {self.attr}: {actual}'

    @staticmethod
    def status_code(self, actual_code):
        return f'{self._msg} correct status code: {actual_code}'

    @staticmethod
    def project_name(self, actual_name, name):
        return f'{self._msg} matching project name: {actual_name}'

    @staticmethod
    def project_desc(self, actual_desc, desc):
        return f'{self._msg} matching project description: {actual_desc}'

    @staticmethod
    def project_identifier(self, actual_identifier, identifier):
        return f'{self._msg} correct project identifier: {actual_identifier}'

    @staticmethod
    def task_type(self, actual_type, wp_type):
        return f'{self._msg} correct work package type: {actual_type}'

    @staticmethod
    def task_subject(self, actual_subject, subject):
        return f'{self._msg} matching work package subject: {actual_subject}'

    @staticmethod
    def lock_version(self, actual_lock_version, lock_version):
        return f'{self._msg} lockVersion: {actual_lock_version}'
