# C++ configuration

cpp = {
    'extension': ['.cpp', '.h', '.hpp'],
    'icon': '',
    'grammer': {
        'singleWords': '#%^&*()-+/{[]}\\|:;"\'/.,<>~=?!',
        'multiWords': ['int', 'double', 'float', 'long', 'short', 'string', 'class', 'void', 'if', 'for', 'else', 'while', 'namespace', 'using', 'template', 'bool', 'return', 'auto', 'struct', 'friend', 'operator', 'cont', 'continue', 'break', 'true', 'false', 'new', 'delete', 'typename', 'protected', 'public', 'private', 'unsigned', 'typedef', 'static', 'const', 'throw', 'nullptr'],
        'comment': '//',
        'keyWord': ['define', 'ifdef', 'ifndef', 'endif', 'include'],
        'string': ['"', '\''],
        'before': ['('],
        'after': ['class'],
        'special': [],  # configured below
        'color': {
            'symbol': ['red', []],
            'special': ['yellow', ['bold']],
            'microlike': ['green', ['bold']],
            'number': ['magenta', []],
            'string': ['green', []],
            'comment': ['grey', []],
            'BA': ['blue', []],
            'linenumber': ['white', []],
            'clear': ['white', []],
        }
    },
}
cpp['grammer']['special'] = cpp['grammer']['multiWords']
