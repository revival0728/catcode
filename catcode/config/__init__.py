from . import config

default_config = config.DEFAULT

language_list = {
    'cpp': config.cpp,
    'python3': config.python3,
    'javascript': config.javascript
}

language_extension = {
    '.cpp': 'cpp',
    '.h': 'cpp',
    '.hpp': 'cpp',
    '.py': 'python3',
    '.js': 'javascript'
}
