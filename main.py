import PySimpleGUI as sg
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

search = [sg.In(size=(50, 200), font='75', key='url', do_not_clear=False)]
text = [sg.Text(text='Enter youtube url', font=25, pad=(0, 20))]

layout = [text, search, buttons]

window = sg.Window(window_title, layout)

while True:
    event, values = window.read()
    downloader = Downloader()
    url = values['url']

    if event == 'mp4':
        downloader.video(url)

    if event == 'mp3':
        downloader.audio(url)

    if event == 'playlist-mp3':
        downloader.playlist_audio(url)

    if event == 'playlist-mp4':
        downloader.playlist_video(url)

    if event == 'download':
        downloader.run_download()
        window.close()
