from .default_config import DEFAULT
from .cpp_config import cpp
from .python3_config import python3
from .javascript_config import javascript

class Export:
    def language_config(self) -> dict:
        return {
            'cpp': cpp,
            'python3': python3,
            'javascript': javascript,
            'DEFAULT': DEFAULT,
        }

    def language_grammer(self) -> dict:
        language_config = self.language_config()
        language_grammer = {}
        for lan in language_config:
            language_grammer[lan] = language_config[lan]['grammer']
        return language_grammer

    def language_extension(self) -> dict:
        language_config = self.language_config()
        language_extension = {}
        for lan in language_config:
            for ext in language_config[lan]['extension']:
                language_extension[ext] = lan
        return language_extension

    def language_icon(self) -> dict:
        language_config = self.language_config()
        language_icon = {}
        for lan in language_config:
            language_icon[lan] = language_config[lan]['icon']
        return language_icon
