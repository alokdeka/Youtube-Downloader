from subprocess import call


def song(e):
    name = e.get()
    print('Downloading {} song'.format(name))

    search = ["ytsearch:" + name]
    command = ['youtube-dl', '-o', '/home/umang/Music/%(title)s.%(ext)s+']
    audio_format = "-x --audio-format mp3".split()
    search.extend(audio_format)
    command.extend(search)
    call(command, shell=False)
    print()