from . import highlight as hlt

config = {}

def before(line: list) -> list:
    index = []
    for i, o in enumerate(line):
        if o.content.strip() in config['before']:
            index.append(i)
    for i in index:
        if i-1 < 0:
            continue
        if type(line[i-1]) == hlt.Clear:
            line[i-1] = hlt.BA(line[i-1].content)
    return line

def after(line: list) -> list:
    index = []
    for i, o in enumerate(line):
        if o.content.strip() in config['after']:
            index.append(i)
    for i in index:
        if i+1 >= len(line):
            continue
        if type(line[i+1]) == hlt.Clear:
            line[i+1] = hlt.BA(line[i+1].content)
    return line
