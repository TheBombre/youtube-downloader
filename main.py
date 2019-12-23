import PySimpleGUI as sg
import pyperclip
from Downloader import Downloader

window_title = 'Youtube Downloader'
theme = 'DarkAmber'
pad = 10
sg.change_look_and_feel('DarkBlue1')

buttons = [
    sg.Button(
        button_text='mp3', pad=(
            (20, pad), (pad, pad)), font=24
    ),
    sg.Button(button_text='mp4', font=24),
    sg.Button(button_text='playlist-mp3', font=24),
    sg.Button(button_text='playlist-mp4', font=24),
    sg.Button(button_text='download', font=24, key='download', button_color=('white', 'green'))]

input_area = [
    sg.In(size=(50, 200), font='75', key='url', do_not_clear=False),
    sg.Button(button_text='paste', font=24, key='paste')
    ]

text = [sg.Text(text='Enter youtube url', font=25, pad=(0, 20))]

layout = [text, input_area, buttons]

window = sg.Window(window_title, layout)

busy = True

while busy:
    event, values = window.read()
    downloader = Downloader()

    if event == 'paste':
        clipboard_value = pyperclip.paste()
        window.Element('url').Update(clipboard_value)

    if values != None:
        url = values['url']

        # Check chosen format
        if event == 'mp4':
            downloader.video(url)

        if event == 'mp3':
            downloader.audio(url)

        if event == 'playlist-mp3':
            downloader.playlist_audio(url)

        if event == 'playlist-mp4':
            downloader.playlist_video(url)

        if event == 'download':
            busy = False
            downloader.run_download()
            window.close()
    else:
        busy = False
        window.close()
