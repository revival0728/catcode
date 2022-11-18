import sys
from . import config
from . import lib

def fix(lines: list) -> list:
    for line in lines:
        delete = []
        for id, i in enumerate(line):
            if i.content == '':
                delete.append(id)
        delete.reverse()
        for i in delete:
            del line[i]
    return lines

def parse(code: str) -> list:
    lines = lib.seperate.byLine(code)
    for id, i in enumerate(lines):
        lines[id] = lib.seperate.bySpace(i)
    for id, i in enumerate(lines):
        lines[id] = lib.seperate.singleWords(i)
    for id, i in enumerate(lines):
        lines[id] = lib.seperate.multiWords(i)
    for id, i in enumerate(lines):
        lines[id] = lib.seperate.number(i)
    lines = fix(lines)
    for id, i in enumerate(lines):
        lines[id] = lib.segment.keyWord(i)
        lines[id] = lib.segment.string(i)
        lines[id] = lib.segment.comment(i)
    lines = fix(lines)
    for id, i in enumerate(lines):
        lines[id] = lib.BAS.before(i)
    for id, i in enumerate(lines):
        lines[id] = lib.BAS.after(i)
    if lines[-1] == []:
        del lines[-1]

    return lines


def main(fileName: str, language: str = ''):
    try:
        code = lib.IO.readFromFile(fileName)
        if language == '':
            lib.setConfig(config.language_grammer['DEFAULT'])
        else:
            lib.setConfig(config.language_grammer[language])
    except FileNotFoundError:
        print('File Not Found')
        return
    except KeyError:
        print('Unknown Language\nYou can customize yourself!')
        return
    except IsADirectoryError:
        print('Cannot print directory')
        return
    code = lib.IO.merge(parse(code))
    print(code, end = '\n\n')

def getFileExtension(filename: str) -> str:
    lastDotIndex = -1
    for index, s in enumerate(filename):
        if s == '.':
            lastDotIndex = index
    return filename[lastDotIndex:]

def getLanguageName(filename: str) -> str:
    fileExtension = getFileExtension(filename)
    if fileExtension in config.language_extension:
        return config.language_extension[fileExtension]
    else:
        return ''

def CLI() -> None:
    if len(sys.argv) == 1:
        print('Did Not Pass the File Argument')
        return
    printFileIcon = '--icon' in sys.argv
    printFileName = '--name' in sys.argv
    forceLanguage = ''
    for ln in config.langauge_name:
        if f'--flx{ln}' in sys.argv:
            forceLanguage = ln
    for i in sys.argv[1:]:
        if i[0:2] == '--':
            continue
        fileName, language = i, getLanguageName(i)
        if len(forceLanguage) != 0:
            language = forceLanguage
        if printFileName:
            if printFileIcon:
                print(config.language_icon[language], end = ' ')
            print(i)
        main(fileName, language)

if __name__ == '__main__':
    CLI()
