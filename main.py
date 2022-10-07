import config
import lib
import colorama
import sys

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

def main(fileName: str, language: str = ''):
    try:
        code = lib.IO.readFromFile(fileName)
        if language == '':
            lib.setConfig(config.default_config)
        else:
            lib.setConfig(config.language_list[language])
    except FileNotFoundError:
        print('File Not Found')
        return
    except KeyError:
        print('Unknown Language\nYou can customize yourself!')
        return
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
    code = lib.IO.merge(lines)
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

def CLI():
    executable = True
    fileName, language = '', ''
    if len(sys.argv) == 1:
        print('Did Not Pass the File Argument')
        executable = False
    elif len(sys.argv) == 2 and executable:
        fileName, language = sys.argv[1], getLanguageName(sys.argv[1])
    elif executable:
        fileName, language = sys.argv[1], sys.argv[2]
    if executable:
        main(fileName, language)


if __name__ == '__main__':
    colorama.init()
    CLI()
