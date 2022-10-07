from . import highlight as hlt

config = {}

def comment(line: list) -> list:
    if len(config['comment']) == 0:
        return line
    for index in range(len(line)):
        tmp, tmpId = '', index
        while len(tmp) != len(config['comment']) and tmpId < len(line):
            tmp += line[tmpId].content.strip()
            tmpId += 1
        if tmp != config['comment']:
            continue
        for i in range(index, len(line)):
            line[i] = hlt.Comment(line[i].content)
        break
    return line

def keyWord(line: list) -> list:
    hasKeyWord = False
    for i in line:
        if i.content in config['keyWord']:
            hasKeyWord = True
    if not hasKeyWord:
        return line
    for id, i in enumerate(line):
        if type(i) == hlt.Clear:
            line[id] = hlt.MircoLike(i.content)
    return line

def string(line: list) -> list:
    index = []
    delete = []
    bePair = [] # begin-and-end-Pair
    for i, o in enumerate(line):
        if o.content in config['string']:
            index.append(i)
    for id, i in enumerate(index):
        tmp = i-1
        if tmp < 0:
            continue
        while tmp >= 0 and line[tmp].content == '\\':
            tmp -= 1
        if (i - tmp) % 2 == 0:
            delete.append(id)
    delete.reverse()
    for i in delete:
        del index[i]
    bePair.append([])
    for i in index:
        if len(bePair[-1]) == 2:
            bePair.append([])
        if len(bePair[-1]) == 0:
            bePair[-1].append(i)
        else:
            if line[bePair[-1][0]].content == line[i].content:
                bePair[-1].append(i)
    for i in bePair:
        if not len(i) == 2:
            break
        for j in range(i[0], i[1]+1):
            line[j] = hlt.String(line[j].content)
    return line
