import termcolor as tc

config = {}

def highlight(code: list) -> list:
    for line in code:
        for id, i in enumerate(line):
            if i.content in config['special']:
                line[id] = Special(i.content)
    return code

# Syntax highlighting class

class Section:
    def __init__(self, content):
        self.content = content

class Clear(Section):
    def __init__(self, content):
        super().__init__(content)
    def __str__(self):
        return tc.colored(self.content, config['color']['clear'][0], attrs=config['color']['clear'][1])
    def __repr__(self):
        return f'({type(self)}) -> ({self.__str__()})\n'

class Symbol(Section):
    def __init__(self, content):
        super().__init__(content)
    def __str__(self):
        return tc.colored(self.content, config['color']['symbol'][0], attrs=config['color']['symbol'][1])
    def __repr__(self):
        return f'({type(self)}) -> ({self.__str__()})\n'

class Special(Section):
    def __init__(self, content):
        super().__init__(content)
    def __str__(self):
        return tc.colored(self.content, config['color']['special'][0], attrs=config['color']['special'][1])
    def __repr__(self):
        return f'({type(self)}) -> ({self.__str__()})\n'

class MircoLike(Section):
    def __init__(self, content):
        super().__init__(content)
    def __str__(self):
        return tc.colored(self.content, config['color']['microlike'][0], attrs=config['color']['microlike'][1])
    def __repr__(self):
        return f'({type(self)}) -> ({self.__str__()})\n'

class Number(Section):
    def __init__(self, content):
        super().__init__(content)
    def __str__(self):
        return tc.colored(self.content, config['color']['number'][0], attrs=config['color']['number'][1])
    def __repr__(self):
        return f'({type(self)}) -> ({self.__str__()})\n'

class String(Section):
    def __init__(self, content):
        super().__init__(content)
    def __str__(self):
        return tc.colored(self.content, config['color']['string'][0], attrs=config['color']['string'][1])
    def __repr__(self):
        return f'({type(self)}) -> ({self.__str__()})\n'

class Comment(Section):
    def __init__(self, content):
        super().__init__(content)
    def __str__(self):
        return tc.colored(self.content, config['color']['comment'][0], attrs=config['color']['comment'][1])
    def __repr__(self):
        return f'({type(self)}) -> ({self.__str__()})\n'

class BA(Section): # before-after
    def __init__(self, content):
        super().__init__(content)
    def __str__(self):
        return tc.colored(self.content, config['color']['BA'][0], attrs=config['color']['BA'][1])
    def __repr__(self):
        return f'({type(self)}) -> ({self.__str__()})\n'
