import PySimpleGUI as sg
from Downloader import Downloader

window_title = 'Youtube Downloader'
theme = 'DarkAmber'
pad = 10
sg.change_look_and_feel('DarkBlue1')

buttons = [
    sg.Button(
        button_text='mp3', pad=(
            (50, pad), (pad, pad)), font=24
    ),
    sg.Button(button_text='mp4', font=24),
    sg.Button(button_text='playlist-mp3', font=24),
    sg.Button(button_text='playlist-mp4', font=24)]

search = [sg.In(size=(50, 200), font='75', key='url')]
text = [sg.Text(text='Enter youtube url', font=25, pad=(0, 20))]

layout = [text, search, buttons]

window = sg.Window(window_title, layout)

while True:
    event, values = window.read()
    downloader = Downloader()
    url = values['url']

    if event == 'mp4':
        downloader.video_format(download_playlist=False)

    elif event == 'mp3':
        downloader.audio_format(download_playlist=False)

    elif event == 'playlist-mp3':
        downloader.playlist_audio_format()

    elif event == 'playlist-mp4':
        downloader.playlist_video_format()

    downloader.download(url)
    del downloader

window.close()
