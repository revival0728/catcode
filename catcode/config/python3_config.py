# Python3 configuration

python3 = {
    'extension': ['.py'],
    'icon': '',
    'grammer': {
        'singleWords': '#%^&*()-+/{[]}\\|:;"\'/.,<>~=?!',
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
    },
}
python3['grammer']['special'] = python3['grammer']['multiWords']
