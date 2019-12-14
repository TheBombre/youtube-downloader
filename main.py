import subprocess


def downloader():
    youtube_search_names = read_file()

    no_of_searches = len(youtube_search_names)

    for index in range(no_of_searches):

        command = ['youtube-dl',
                   '-o',
                   './downloads/%(title)s.%(ext)s',
                   '-x',
                   '--audio-format',
                   'mp3'
                   ]

        video_name = youtube_search_names[index].strip()
        search_option = f'ytsearch:{video_name}'

        command.append(search_option)

        print(f'\n Downloading song {index + 1} out of {no_of_searches} \n')
        subprocess.call(command)


def read_file():
    source_file = open('test.txt', 'r')

    youtube_search_names = source_file.readlines()
    source_file.close()

    return youtube_search_names


downloader()
