import sys

config = {}

if sys.platform == 'win32':
    config['outtmpl'] = "C:\\Users\\barbr\\Downloads\\"
elif sys.platform == 'darwin':
    config['outtmpl'] = '/Users/carlton/Downloads/'

