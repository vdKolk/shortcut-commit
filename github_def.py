import os
from shortcut_def import Shortcut


class GitHub:
    @staticmethod
    def __add_all_to_commit() -> None:
        os.popen(f'git -C {os.getcwd()} add .')

    @staticmethod
    def create_commit() -> None:
        title = Shortcut().get_shortcut_story_title()
        story_number = Shortcut.get_story_number()

        GitHub.__add_all_to_commit()

        os.popen(f'git -C {os.getcwd()} commit -m "Fixes [sc-{story_number}] {title}" --no-verify')
        os.popen(f'git -C {os.getcwd()} push -u origin feature-develop/sc-{story_number}')
