import termcolor as tc
import math

config = {}

def readFromFile(fullFileName):
    with open(fullFileName, 'r', encoding='utf-8') as f:
        return f.read()

def calcExpectLength(lenOfList: int) -> int:
    return int(math.log10(lenOfList)) + 1

def fixLineNumber(lineNumber: int, expectLength: int) -> str:
    lineNumber = str(lineNumber)
    while len(lineNumber) < expectLength:
        lineNumber = ' ' + lineNumber
    return lineNumber

def merge(lines: list) -> str:
    while lines[-1] == []:
        del lines[-1]
    expectLength = calcExpectLength(len(lines))
    for id, i in enumerate(lines):
        tmp = ''
        for j in i:
            tmp += str(j)
        lines[id] = tmp
    for ln, i in enumerate(lines):
        lines[ln] = f"{str(tc.colored(f'{fixLineNumber(ln+1, expectLength)} |', config['color']['linenumber'][0], attrs=config['color']['linenumber'][1]))} {''.join(i)}"
    return '\n'.join(lines)
