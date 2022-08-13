import main
import sys

if __name__ == '__main__':
    executable = True
    fileName, language = '', ''
    print(len(sys.argv))
    if len(sys.argv) == 1:
        print('Did Not Pass the File Argument')
        executable = False
    elif len(sys.argv) == 2 and executable:
        fileName = sys.argv[1]
    elif executable:
        fileName, language = sys.argv[1], sys.argv[2]
    if executable:
        main.main(fileName, language)
