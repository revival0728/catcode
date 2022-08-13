empty = {
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

cpp = {
    'singleWords': '#%^&*()-+/{[]}\\|:;"\'/.,<>~=?',
    'multiWords': ['int', 'double', 'float', 'long', 'short', 'string', 'class', 'void', 'if', 'for', 'else', 'while', 'namespace', 'using', 'template', 'bool', 'return', 'auto', 'struct', 'friend', 'operator', 'cont', 'continue', 'break', 'true', 'false', 'new', 'delete', 'typename', 'protected', 'public', 'private', 'unsigned'],
    'comment': '//',
    'keyWord': ['define', 'ifdef', 'ifndef', 'endif', 'include'],
    'string': ['"', '\''],
    'before': ['('],
    'after': ['class'],
    'special': ['int', 'double', 'float', 'long', 'short', 'string', 'class', 'void', 'if', 'for', 'else', 'while', 'namespace', 'using', 'template', 'bool', 'return', 'auto', 'struct', 'friend', 'operator', 'cont', 'continue', 'break', 'true', 'false', 'new', 'delete', 'typename', 'protected', 'public', 'private', 'unsigned'],
    'color': {
        'symbol': ['red', []],
        'special': ['yellow', ['bold']],
        'microlike': ['green', ['bold']],
        'number': ['magenta', []],
        'string': ['green', []],
        'comment': ['grey', []],
        'BA': ['blue', []],
        'linenumber': ['grey', []],
        'clear': ['white', []],
    }
}
