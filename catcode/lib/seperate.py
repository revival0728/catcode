from . import highlight as hlt

config = {}

def byLine(code: str) -> list:
    return code.strip('\n').split('\n')

def bySpace(line: str) -> list:
    SPACE_4 = ' '*4
    while SPACE_4 in line:
        line = line.replace(SPACE_4, '\t')
    tmp = line.strip(' ').split(' ')
    ret = []
    for i in tmp:
        ret.append(i.replace('\t', SPACE_4))
        ret.append(' ')
    del ret[-1]
    return ret

def singleWords(section: str) -> list:
    ret = []
    tmp = ''
    for s in section:
        for i in s:
            if i in config['singleWords']:
                ret.append(hlt.Clear(tmp))
                ret.append(hlt.Symbol(i))
                tmp = ''
            else:
                tmp += i
        ret.append(hlt.Clear(tmp))
        tmp = ''
    return ret

def multiWords(line: list) -> list:
    for id, section in enumerate(line):
        if not isinstance(section, hlt.Clear):
            continue
        if section.content.strip() in config['multiWords']:
            line[id] = hlt.Special(section.content)
    return line

def number(line: list) -> list:
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for id, section in enumerate(line):
        if not isinstance(section, hlt.Clear) or len(section.content) < 1:
            continue
        if section.content[0] in numbers:
            line[id] = hlt.Number(section.content)
    return line
