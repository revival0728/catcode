# You can copy the EMPTY configuration to start your customizations

# A empty configuration
EMPTY = {
    'singleWords': '',
    'multiWords': [],
    'comment': '',
    'keyWord': [],
    'string': [],
    'before': [],
    'after': [],
    'special': [],

    # color
    #     - grey
    #     - red
    #     - green
    #     - yellow
    #     - blue
    #     - magenta
    #     - cyan
    #     - white
    # attrs
    #     - bold
    #     - dark
    #     - underline
    #     - blink
    #     - reverse
    #     - concealed
    'color': {
        'symbol': [],
        'special': [],
        'microlike': [],
        'number': [],
        'string': [],
        'comment': [],
        'BA': [],   # before and after
        'linenumber': [],
        'clear': [],
    }
}


# DEFAULT configuration
DEFAULT = {
    'singleWords': '#%^&*()-+/{[]}\\|:;"\'/.,<>~=?`$',
    'multiWords': [],
    'comment': '',
    'keyWord': [],
    'string': [],
    'before': [],
    'after': [],
    'special': [],
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
}


# C++ configuration
cpp = {
    'singleWords': '#%^&*()-+/{[]}\\|:;"\'/.,<>~=?',
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
}
cpp['special'] = cpp['multiWords']


# Python3 configuration
python3 = {
    'singleWords': '#%^&*()-+/{[]}\\|:;"\'/.,<>~=?',
    'multiWords': ['int', 'float', 'str', 'class', 'if', 'for', 'else', 'elif', 'while', 'bool', 'return', 'cont', 'continue', 'break', 'True', 'False', 'del', 'async', 'import', 'as', 'def', 'try', 'except', 'not', 'in', 'with', 'from', 'None', 'lambda', 'raise'],
    'comment': '#',
    'keyWord': [],
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
}
python3['special'] = python3['multiWords']
