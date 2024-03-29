from youtube_dl import YoutubeDL
import concurrent.futures
from pytube import Playlist
from config import config


class Downloader:
    audio_downloads = []
    video_downloads = []
    playlist_audio_downloads = []
    playlist_video_downloads = []

    def __init__(self):
        self.audio_ydl_options = {
            'format': 'bestaudio/best',
            'outtmpl': '{}%(title)s.%(ext)s'.format(config['outtmpl']),
            'ignoreerrors': True,
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        self.video_ydl_options = {
            'format': 'bestaudio/best',
            'outtmpl': '{}%(title)s.%(ext)s'.format(config['outtmpl']),
            'ignoreerrors': True,
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        }
    # Adding chosen format to corresponding list so they can be downloaded together 
    def audio(self, url):
        self.audio_downloads.append(url)

    def video(self, url):
        self.video_downloads.append(url)

    def playlist_audio(self, url):
        self.playlist_audio_downloads.append(url)

    def playlist_video(self, url):
        self.playlist_video_downloads.append(url)

    # So all videos can be donwloaded at the same time instead of individually
    def load_playlist_urls(self, playlists):
        all_playlist_urls = []

        for playlist in playlists:
            p = Playlist(playlist)
            p.populate_video_urls()
            urls = p.video_urls
            all_playlist_urls.extend(urls)

        return all_playlist_urls

    def single_download(self, url, options):
        ydl = YoutubeDL(options)
        ydl.download([url])

    def concurrent_download(self, urls, options):

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for url in urls:
                executor.submit(self.single_download, url, options)

    def run_download(self):
        # Only runs when video url has been submitted for download in the lists

        if len(self.audio_downloads) > 0:
            print('downloading audio')
            self.concurrent_download(urls=self.audio_downloads,
                                     options=self.audio_ydl_options)

        if len(self.video_downloads) > 0:
            self.concurrent_download(urls=self.video_downloads,
                                     options=self.video_ydl_options)

        if len(self.playlist_audio_downloads) > 0:
            playlist_options = self.audio_ydl_options.copy()
            
            # Ensure the whole playlist is donwloaded, not one video
            del playlist_options['noplaylist']

            urls = self.load_playlist_urls(self.playlist_audio_downloads)

            self.concurrent_download(urls=urls,
                                     options=playlist_options)

        if len(self.playlist_video_downloads) > 0:
            playlist_options = self.video_ydl_options.copy()

            # Ensure the whole playlist is donwloaded, not one video
            del playlist_options['noplaylist']

            urls = self.load_playlist_urls(self.playlist_video_downloads)

            self.concurrent_download(urls=urls,
                                     options=playlist_options)
