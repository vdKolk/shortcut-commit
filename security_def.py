import os


class Security:
    def __init__(self, keys=None) -> None:
        self.keys = keys

    def __get_tokens_from_storage(self) -> None:
        file = open(f'{os.path.dirname(os.path.abspath(__file__))}/storage/secrets', 'r')
        self.keys = file.readline().split(';')
        file.close()

    def __get_key(self, index) -> str:
        self.__get_tokens_from_storage()

        if self.keys[index] is None:
            raise LookupError('One of the keys is not set, run setup.py')

        return self.keys[index]

    def get_shortcut_token(self) -> str:
        return self.__get_key(1)

    def get_github_token(self) -> str:
        return self.__get_key(0)