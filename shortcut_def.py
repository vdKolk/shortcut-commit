import os
import re
import requests


class Shortcut:

    SHORTCUT_BASE_URL = 'https://api.app.shortcut.com/api/v3'

    def __init__(self, key) -> None:
        self.key = key

    def get_shortcut_story_title(self) -> str:
        res = requests.get(
            f'{self.SHORTCUT_BASE_URL}/stories/{Shortcut.__get_story_number()}',
            headers={
                "Content-Type": "application/json",
                "Shortcut-Token": "6460e5f6-5485-4ee2-bd37-012856e91496"
            }
        )

        return res.json()['name']

    @staticmethod
    def __get_story_number() -> int | bool:
        stream = os.popen(f'git -C {os.getcwd()} rev-parse --abbrev-ref HEAD')

        matches = re.findall('\d{5}', stream.read())

        return matches[0] if len(matches) == 1 else False
