import os


class Security:
    """Class providing interaction abilities to the stored security details"""

    def __init__(self, key=None) -> None:
        self.key = key

    def __get_tokens_from_storage(self) -> None:
        with open(
            f'{os.path.dirname(os.path.abspath(__file__))}/storage/secrets',
            'r',
            encoding='UTF-8'
        ) as file:
            self.key = file.readline()
            file.close()

    def __get_key(self) -> str:
        self.__get_tokens_from_storage()

        if self.key is None:
            raise LookupError('One of the keys is not set, run setup.py')

        return self.key

    def get_shortcut_token(self) -> str:
        return self.__get_key()
