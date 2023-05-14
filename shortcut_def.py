import os, re


class Shortcut:
    def __init__(self, key) -> None:
        self.key = key

    @staticmethod
    def get_story_number() -> int | bool:
        stream = os.popen(f'git -C {os.getcwd()} rev-parse --abbrev-ref HEAD')

        matches = re.findall('\d{5}', stream.read())

        return matches[0] if len(matches) == 1 else False
