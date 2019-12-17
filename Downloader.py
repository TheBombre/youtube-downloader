import subprocess


class Downloader:
    default = ['youtube-dl', '-o', './downloads/%(title)s.%(ext)s', ]

    def __init__(self):
        self.command = self.default.copy()

    def audio_format(self, download_playlist):
        audio_options = ['-x', '--audio-format', 'mp3']

        if not(download_playlist):
            audio_options.append('--no-playlist')

        self.command.extend(audio_options)

    def video_format(self, download_playlist):
        video_options = ['-f', 'mp4']

        if not(download_playlist):
            video_options.append('--no-playlist')

        self.command.extend(video_options)

    def playlist_audio_format(self):
        self.audio_format(download_playlist=True)
        self.command.append('--yes-playlist')

    def playlist_video_format(self):
        self.video_format(download_playlist=True)
        self.command.append('--yes-playlist')

    def download(self, url):
        self.command.append(url)
        print(self.command)
        subprocess.call(self.command)
