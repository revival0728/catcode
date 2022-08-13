from . import highlight as hlt

config = {}

def byLine(code: str) -> str:
    return code.strip(' ').split('\n')

def bySpace(line: str) -> str:
    line = line.replace(' '*4, '\t')
    tmp = line.strip(' ').split(' ')
    ret = []
    for i in tmp:
        ret.append(i)
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

def multiWords(line: hlt.Clear) -> list:
    for id, section in enumerate(line):
        if type(section) != hlt.Clear:
            continue
        if section.content.strip() in config['multiWords']:
            line[id] = hlt.Special(section.content)
    return line

def number(line: hlt.Clear) -> list:
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    for id, section in enumerate(line):
        if type(section) != hlt.Clear or len(section.content) < 1:
            continue
        if section.content[0] in numbers:
            line[id] = hlt.Number(section.content)
    return line
