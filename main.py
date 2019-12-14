import subprocess


def downloader():
    songs = read_file()
    no_of_songs = len(songs)

    command = ['youtube-dl',
               '-o',
               './downloads/%(title)s.%(ext)s',
               '-x',
               '--audio-format',
               'mp3',
               ]

    for index in range(no_of_songs):
        song_name = songs[index].strip()
        search_query = f'ytsearch:{song_name}'

        command.append(search_query)

        print(f'\n Downloading song {index + 1} out of {no_of_songs} \n')
        subprocess.call(command)


def read_file():
    song_list_file = open('songs.txt', 'r')

    songs = song_list_file.readlines()
    song_list_file.close()

    return songs


downloader()
