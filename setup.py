import sys
import os
from PyInstaller.__main__ import run

run([
    '--name=%s' % 'Youtube Downloader',
    '--onefile',
    '--windowed',
    '--icon=%s' % os.path.join('resources', 'icon.ico'),
    os.path.join('main.py'),
])
