import os
from shortcut_def import Shortcut


class GitHub:
    """Class providing interaction abilities to GitHub via the CLI"""

    @staticmethod
    def __add_all_to_commit() -> None:
        os.system(f'git -C {os.getcwd()} add .')

    @staticmethod
    def create_commit() -> None:
        title = Shortcut().get_shortcut_story_title()
        story_number = Shortcut.get_story_number()

        GitHub.__add_all_to_commit()

        os.system(f'git -C {os.getcwd()} commit -m "Fixes [sc-{story_number}] {title}"')
        os.system(f'git -C {os.getcwd()} push -u origin feature-develop/sc-{story_number}')

    @staticmethod
    def amend_commit() -> None:
        GitHub.__add_all_to_commit()

        os.system(f'git -C {os.getcwd()} commit --amend --no-edit')
        os.system(f'git -C {os.getcwd()} push -f')
