import getpass
import os


# Customize
DELETE_ORIGINAL_FILES = True


class Config:

    def __init__(self):
        self.usr_name = self.get_usr_name()
        self.usr_home = os.path.join(r'C:\Users', self.usr_name)
        self.usr_downloads = os.path.join(self.usr_home, 'Downloads')
        self.bad_suffix = self.bad_suffix()
        self.test = r"C:\Users\ZP\Pictures\Saved Pictures\tmp\test"

    @staticmethod
    def get_usr_name():
        return getpass.getuser()

    @staticmethod
    def bad_suffix():
        block_words = """
        ini
        """.strip().split()
        return block_words
