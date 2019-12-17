import sys
from cx_Freeze import setup, Executable

base = None
# if sys.platform == 'win32':
base = 'Win32GUI'

executables = [
    Executable('main.py', base=base)
]

setup(name='Youtube Downloader',
      version='0.1',
      description='downloading youtube videos as videos or audios',
      executables=executables
      )
