# javascript configuration

javascript = {
    'extension': ['.js'],
    'icon': '',
    'grammer': {
        'singleWords': '#%^&*()-+/{[]}\\|:;"\'/.,<>~=?$!',
        'multiWords': ['if', 'import', 'else', 'for', 'while', 'class', 'None', 'Boolean', 'return', 'const', 'continue', 'break', 'true', 'false', 'String', 'var', 'function', 'document', 'from', 'export', 'let', 'Object', 'async', 'default', 'await', 'undefined', 'null'],
        'comment': '//',
        'keyWord': [],
        'string': ['"', '\'', '`'],
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
javascript['grammer']['special'] = javascript['grammer']['multiWords']
